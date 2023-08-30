#Program will specify whether a user-entered variable name is
    # illegal (no spaces allowed, must begin with a letter)
    # legal, but uses poor style (should only use letters or digits)
    # good 
variable = " "

print ("Properness of a Proposed Variable Name.")
variable = input("Enter a proper variable name (q to quit):")
while variable !="q":
    if " " in variable: 
        print ("Illegal")
    elif "1" in variable [0:1]:
        print ("Illegal")
    elif "2" in variable [0:1]:
        print ("Illegal")
    elif "3" in variable [0:1]:
        print ("Illegal")
    elif "4" in variable [0:1]:
        print ("Illegal")
    elif "5" in variable [0:1]:
        print ("Illegal")
    elif "6" in variable [0:1]:
        print ("Illegal")
    elif "7" in variable [0:1]:
        print ("Illegal")
    elif "8" in variable [0:1]:
        print ("Illegal")
    elif "9" in variable [0:1]:
        print ("Illegal")
    elif "0" in variable [0:1]:
        print ("Illegal")
    elif "!" in variable: 
        print ("Legal")
    elif "." in variable: 
        print ("Legal")
    elif "@" in variable: 
        print ("Legal")
    elif "#" in variable: 
        print ("Legal")
    elif "%" in variable: 
        print ("Legal")
    elif "^" in variable: 
        print ("Legal")
    elif "&" in variable: 
        print ("Legal")
    elif "*" in variable: 
        print ("Legal")
    elif "(" in variable: 
        print ("Legal")
    elif ")" in variable: 
        print ("Legal")
    elif "_" in variable: 
        print ("Legal")
    elif "+" in variable: 
        print ("Legal")
    elif "," in variable: 
        print ("Legal")
    elif "/" in variable: 
        print ("Legal")
    else:
        print ("Good")
    variable = input("Enter a proper variable name (q to quit):")