# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

username = ""
password = ""
while username != "admin" and password != "admin":
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Output:
    # Enter your username: sneha
    # Enter your password: 
    # Enter your username: snhea
    # Enter your password: snjsm
    # Enter your username: admin
    # Enter your password: admin

    
