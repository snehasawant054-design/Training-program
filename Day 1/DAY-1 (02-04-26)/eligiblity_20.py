#WAP to accept phy, chem,and maths,subject marks calculate total and percentageand if percentage is greater then equal to 60 and gender is equal to male so he is eligible for placement elase eligeble for data entry job.

phy = float(input("Enter physics marks: "))
chem = float(input("Enter chemistry marks: "))
maths = float(input("Enter maths marks: "))
gender = input("Enter gender (male/female): ")
total = phy + chem + maths
percentage = (total / 300) * 100
if percentage >= 60 and gender.lower() == "male":
    print("Eligible for placement")
else:
    print("Eligible for data entry job")

    # Output1:
    # Enter physics marks: 70
    # Enter chemistry marks: 80
    # Enter maths marks: 90
    # Enter gender (male/female): male
    # Eligible for placement  
    # Output2:
    #Enter physics marks: 50
    # Enter chemistry marks: 60
    # Enter maths marks: 30
    # Enter gender (male/female): male
    # Eligible for data entry job  





