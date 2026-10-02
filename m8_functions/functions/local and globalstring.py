case_rule = "lower"  # global variable
def clean_name(name):   #parameter 
    cleaned = name.strip()          #local variable + function
    if case_rule == "lower":        #condition
        cleaned = cleaned.lower()
    print("Cleaned:", cleaned)

clean_name("  MaariAAA ")
print("The rule is:", case_rule)