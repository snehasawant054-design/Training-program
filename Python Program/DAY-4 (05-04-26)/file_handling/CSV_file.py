import csv
f = open("student.csv","a",newline="")
a = csv.writer(f)
# a.writerow(["studid","rollno","name","mobno"])

studentid = int(input("Enter student id : "))
rollno = int(input("Enter roll number : "))
name = input("Enter name : ")
mobno = int(input("Enter mobile number : "))

a.writerow([studentid,rollno,name,mobno])
print("student record has saved")

# Output:
# Enter student id : 101
# Enter roll number : 43
# Enter name : sneha
# Enter mobile number : 9403274709
# student record has saved

