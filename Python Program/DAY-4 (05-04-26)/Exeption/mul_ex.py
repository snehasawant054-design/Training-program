try:
    n1 = int(input("Enter first value : "))
    n2 = int(input("Enter second value : "))
    print(n1/n2)
except ZeroDivisionError:
    print("Not Divide By Zero.")
except ValueError:
    print("Enter only interger value.")

print("To be continue")

# Output:
# Enter first value : 10
# Enter second value : 0
# Not Divide By Zero.
# To be continue