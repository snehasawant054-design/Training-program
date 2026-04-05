# f = open("file.txt", "w")
# print("Name of File : ", f.name)
# print("Mode of File : ", f.mode)
# print("Readable : ", f.readable())
# print("Writable : ", f.writable())
# print("Is File Closed : ", f.closed)
# f.close()
# print("Is File Closed : ", f.closed)

# Output:
# Name of File :  file.txt
# Mode of File :  w
# Readable :  False
# Writable :  True
# Is File Closed :  False
# Is File Closed :  True

# Writing the file
# f = open("file.txt", "w")
# f.write("\n sneha sawal")
# f.close()
# print("file created successfully")

# Output:
# file created successfully

# Appending the file
# f = open("file.txt", "a")
# f.write("\n sneha sawal")
# f.close()
# print("file appended successfully")

# Output:
# file appended successfully

#read the file
f = open("file.txt", "r")
print(f.read())
f.close()

# Output:
# sneha sawant
# sneha sawal

