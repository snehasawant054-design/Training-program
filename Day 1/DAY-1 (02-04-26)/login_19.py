username = input("enter name:")
password = input("enter password:")
if username == password:
    print("login successful")
else:
    print("login failed")

    # Output1:
    # enter name:sneha
    # enter password:sneha
    # login successful
    # Output2:
    # enter name:sneha
    # enter password:abc123
    # login failed