from re import sub, split
from sys import argv

def __convert_string(input_str,data):
    if(input_str.strip() == "" or input_str.strip()[0] == '#'): return None;
    if('|' in input_str and not ',' in input_str):
        return __convert_object(input_str,data)
    if input_str.startswith('"') and input_str.endswith('"') and input_str.count('"') == 2:
        input_str = input_str[1:-1]
        return input_str
    if input_str.count("ptr%") == 1 and not (',' in input_str):
        nm = input_str.replace("ptr%","")
        return data[nm]
    try:
        return int(input_str)
    except ValueError:
        try:
            return float(input_str)
        except ValueError:
            if input_str.lower() == "true":
                return True
            elif input_str.lower() == "false":
                return False
            elif input_str.count(",") != 0:
                return [__convert_string(value.strip(),data) for value in input_str.split(",") if __convert_string(value.strip(),data) != None]
            else:
                print(f"DNML: Unknown syntax, invalid data type for {input_str}")

def __convert_object(content,data):
    try:
        finalobj = {}
        for val in content.strip().split("|"):
            if(val.strip() == ""): continue
            prop,dat = val.split(":")
            finalobj[prop.strip()]=__convert_string(dat,data)
        return finalobj
    except: return __convert_string(content,data)

def __remove_whitespace_except_quotes(text):
    pattern = r'\s+(?=(?:[^"]*"[^"]*")*[^"]*$)'
    result = sub(pattern, '', text)
    return result

def parse_dnml(data):
    data = data.replace("\n","")
    lines = split('[;]',data)
    final = {}
    for line in lines:
        line = __remove_whitespace_except_quotes(line)
        if(line.startswith("#") or line == ""):
            continue
        try:
            propertyname, content = line.split("-",1)
        except ValueError:
            print("DNML: Unknown Syntax, missing value")
            return {}
      
        final[propertyname] = __convert_string(content,final);
    return final

def stringify_dnml(obj,child = False):
    result = ""
    postfix = '|' if child else ';'
    eq = ':' if child else '-'
    for key in obj:
        if isinstance(obj[key],str):
            result+=f'{str(key)} {eq} "{str(obj[key])}"{postfix}'+"\n"
        elif isinstance(obj[key], int) or isinstance(obj[key], float):
            result+=f'{str(key)} {eq} {str(obj[key])}{postfix}'+"\n"
        elif isinstance(obj[key], list):
            listrep = ""
            for k in obj[key]:
                if(isinstance(k,dict)):
                    listrep+=f'{stringify_dnml(k,True)},'
                else:
                    listrep+=f'{k},'
            listrep = listrep.strip(',')
            dnml_rep = f'{str(key)} {eq} {listrep}{postfix}'
            result+=dnml_rep+"\n"
        elif isinstance(obj[key], dict):
            dictrep = stringify_dnml(obj[key],True)
            dnml_rep = f'{str(key)} {eq} {dictrep}{postfix}'
            result+=dnml_rep+"\n"
        else: print(f"Data Type {type(obj[key])} not supported yet in DNML");
    result = result.strip("\n").strip()
    return result

if __name__ == "__main__":
    if(len(argv) == 2):
        try:
            with open(argv[1],'r') as f:
                print(parse_dnml(f.read()))
        except: print("DNML: Failed to Parse File")
    else:
        try:
            print("DNML Shell Parser\nCreated by Vardan Petrosyan\n")
            while(True):
                str = input("DNML %-> ")
                if(str == "exit"): exit()
                print(parse_dnml(str))
        except KeyboardInterrupt:   pass