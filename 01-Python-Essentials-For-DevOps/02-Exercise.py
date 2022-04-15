# Write a Python function that takes a string as an argument and prints
# whether it is upper or lower case 

def is_upper_or_lower(s):
    up = s.upper()
    low = s.lower()

    if up == s:
        print("It's upper case")
    elif low == s:
        print("It's lower case")
    else:
        print("It's mixed case")

is_upper_or_lower("STEVE")
is_upper_or_lower("steve")
is_upper_or_lower("Steve")