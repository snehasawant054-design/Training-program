#nested if else: WAP to accept value of a,b and c and find max value
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))   
c = float(input("Enter the third number: "))
if a > b:
    if a > c:
        print("The largest number is:", a)
    else:
        print("The largest number is:", c)
else:
    if b > c:
        print("The largest number is:", b)
    else:
        print("The largest number is:", c)

    # Output1:
    # Enter the first number: 10
    # Enter the second number: 5
    # Enter the third number: 20
    # The largest number is: 20.0
    # Output2:
    # Enter the first number: 15
    # Enter the second number: 25
    # Enter the third number: 5
    # The largest number is: 25.0

