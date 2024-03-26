# DNML
Data Notation Markup Language is a Markup Language with a very simple syntax for storing data (similar to JSON)\
I've made a simple parser using python to convert Python dictionaries to DNML files, and vice versa

## Usage
Include `dnml.py` in your environment
```
import dnml
```

DNML has 2 functions `parse_dnml(str)` (converts DNML to dictionary), and `stringify_dnml(dict)` (converts dictionary to DNML)

## Basic Syntax
```
# comment ;
key - value;
```

## Basic Example
```
# This is a comment and yes, comments also end by a semicolon;

name - "John Doe";
age - 30;
height - 5.11;

# this is an array ;
colors -
    "red",
    "green",
    "blue";

# this is an object ;
job -
    name: "Painter" |
    years_experience: 5|
    professional: true;

# this is an array of objects ;
friends - 
    name: "Jacob"|
    surname: "Parsons",
    name: "David"|
    surname: "Jackson";

```
