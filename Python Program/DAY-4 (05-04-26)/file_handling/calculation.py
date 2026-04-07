import csv
f = open("calculation.csv","a",newline="")
a = csv.writer(f)
a.writerow(["name","rollno","mobileno","p1","p2","p3","total","per","result"])

name = input("Enter your name : ")
rollno = int(input("Enter your roll number : "))
mobileno = int(input("Enter your mobile number : "))
p1 = int(input("Enter your marks in p1 : "))
p2 = int(input("Enter your marks in p2 : "))
p3 = int(input("Enter your marks in p3 : "))

total = p1+p2+p3
per = total/3
if p1>=40 and p2>=40 and p3>=40:
    result = "pass"
else:
    result = "fail"
a.writerow([name,rollno,mobileno,p1,p2,p3,total,per,result])
print("student record has saved")






