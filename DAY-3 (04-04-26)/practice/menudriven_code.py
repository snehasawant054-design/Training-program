def add():
    val1 = int(input("Enter the value of val1 : "))
    val2 = int(input("Enter the value of val2 : "))
    print("add = ",val1 + val2)

def sub():
    val1 = int(input("Enter the value of val1 : "))
    val2 = int(input("Enter the value of val2 : "))
    print("sub = ",val1 - val2)

def mul():
    val1 = int(input("Enter the value of val1 : "))
    val2 = int(input("Enter the value of val2 : "))
    print("mul = ",val1 * val2)

def div():
    val1 = int(input("Enter the value of val1 : "))
    val2 = int(input("Enter the value of val2 : "))
    print("div = ",val1 / val2)

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        break

# Output:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
# Enter your choice : 1
# Enter the value of val1 : 10
# Enter the value of val2 : 10
# add =  20
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
# Enter your choice : 3
# Enter the value of val1 : 10
# Enter the value of val2 : 10
# mul =  100
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
# Enter your choice :


    