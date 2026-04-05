try:
    n1 = int(input("Enter first value : "))
    n2 = int(input("Enter second value : "))
    print(n1/n2)
except (ZeroDivisionError,ValueError) as msg:
    print("Enter Correct Number : ",msg)
else:
    print("This is else part of try block")
finally:
    print("I will execute always")

# Output:
# Enter first value : 10
# Enter second value : 5
# 2.0
# This is else part of try block
# I will execute always