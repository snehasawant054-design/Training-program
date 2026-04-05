try:
    n1 = int(input("Enter first value : "))
    n2 = int(input("Enter second value : "))
    try:
        print(n1/n2)
    except ZeroDivisionError as msg:
        print("Enter Correct Number : ",msg)
except ValueError as msg:
    print("Enter Correct Number : ",msg)
finally:
    print("I will execute always")

    # Output:
# Enter first value : 10
# Enter second value : 0
# Enter Correct Number :  division by zero
# I will execute always