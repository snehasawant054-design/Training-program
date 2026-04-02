#accept any character uppercase and lowercase using askycode
char = input("Enter any character:")
if (ord(char) >= 48 and ord(char) <= 57):
    print("Its an integer")
elif (ord(char) >= 65 and ord(char) <= 90) or (
    ord(char) >= 97 and ord(char) <= 122):
    print("Its a string")
else:
    print("Its a special symbol")

    #Output1:
    # Enter character: A
    # Uppercase letter
    # Output2:
    # Enter character: a
    # Lowercase letter
    # Output3:
    # Enter character: 1
    # Not a letter

    