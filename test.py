import dnml

obj = {
    "users":[
        {
            "username":"Vardan2009",
            "usersince":"2019"
        },
        {
            "username":"testacc23",
            "usersince":"2023"
        },
        20
    ]
}

dnml_rep = dnml.stringify_dnml(obj);
print(dnml_rep)
print(dnml.parse_dnml(dnml_rep))