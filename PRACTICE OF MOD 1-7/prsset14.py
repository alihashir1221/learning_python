'''
Duplicate files

Given:
file_list = ["report.csv", "data.xlsx", "report.csv", "notes.txt", "data.xlsx"]
Use a loop to find and print the duplicate filenames only once.

Expected:
report.csv
data.xlsx

For #4, try to build the logic yourself first—you've already started learning exactly this problem.
'''
file_list = ["report.csv", "data.xlsx", "report.csv", "notes.txt", "data.xlsx"]
for file in file_list:
    if file_list.count(file)>1:
        print(f"Duplicate files found: {file}")