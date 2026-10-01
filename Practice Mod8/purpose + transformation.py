'''
Q3 — Purpose + Transformation
Write a function convert_to_upper(text) that:
- Takes a string.
- Converts it to uppercase.
- Returns the transformed string.
- Example: convert_to_upper("python") → "PYTHON"
'''
def convert_to_upper(text):
    upper_case = text
    return upper_case.upper()
username = input("Enter yor name: ")
print(convert_to_upper(username))