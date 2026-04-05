try:
    n1 = int(input("Enter first value : "))
    n2 = int(input("Enter second value : "))
    print(n1/n2)
except (ZeroDivisionError,ValueError) as msg:
    print("Enter Correct Number : ",msg)
finally:
    print("This is finally part of try block")

    # Output:
# Enter first value : 10
# Enter second value : 0
# Enter Correct Number :  division by zero
# This is finally part of try block

