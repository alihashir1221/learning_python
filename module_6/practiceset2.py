#WAP to find out wether a student has passed or failed if it requires total of 40% and at least 33% in each subject to pass.
#Assume 3 subjects and take marks as an input from the user.
subject1 = int(input("Enter subject 1 marks out of 100: "))
subject2 = int(input("Enter subject 2 marks out of 100: "))
subject3 = int(input("Enter subject 3 marks out of 100: "))
# if (((subject1 + subject2 + subject3)/300)*100 >= 40) and ((subject1/100)*100 >= 33) and ((subject2/100)*100 >= 33) and ((subject3/100)*100 >= 33):
total_percentage = (((subject1 + subject2 + subject3) / 300) * 100)
if(total_percentage >= 40 and subject1 >= 33 and subject2 >= 33 and subject3 >= 33):
    print("Pass")
else:
    print("Fail")
