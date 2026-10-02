'''
Check wether any filename apperas more than once
    file_list = [
        'report.csv',
        'data.xlsx',
        'summary.docx',
        'report.csv',
        'data.csv'
    ]
Print "Duplicate found" if a duplicate exists, otherwise print "All files are unique."
'''
file_list = [
        'report.csv',
        'data.xlsx',
        'summary.docx',
        'report.csv',
        'data.csv'
    ]
for file in file_list:
    if file_list.count(file)>1:
        print("Duplicate found")
        break
else:
    print("All files are unique.")