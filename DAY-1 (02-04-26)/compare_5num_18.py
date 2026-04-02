n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: ")) 
n3 = float(input("Enter the third number: "))
n4 = float(input("Enter the fourth number: "))
n5 = float(input("Enter the fifth number: "))

largest = n1
if n2 > largest:
    largest = n2
if n3 > largest:
    largest = n3
if n4 > largest:
    largest = n4
if n5 > largest:
    largest = n5

smallest = n1
if n2 < smallest:
    smallest = n2
if n3 < smallest:
    smallest = n3
if n4 < smallest:
    smallest = n4
if n5 < smallest:
    smallest = n5

print("The largest number is:", largest)
print("The smallest number is:", smallest)

# Output:
# Enter the first number: 10
# Enter the second number: 5
# Enter the third number: 20
# Enter the fourth number: 3
# Enter the fifth number: 15
# The largest number is: 20.0
# The smallest number is: 3.0