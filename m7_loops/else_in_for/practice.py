#check wether all the files have .csv extension or not
files = ['data.csv', 'report.csv', 'summary.txt', 'analysis.csv']
for file in files:
    if not file.endswith(".csv"):
        print(f"{file} is not .csv ")
        break
else:
    print("There is no eror")