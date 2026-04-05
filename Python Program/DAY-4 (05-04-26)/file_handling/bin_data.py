f1 = open("panda.jpeg","rb")
f2 = open("panda_copy.jpeg","wb")

data = f1.read()
f2.write(data)

print("New image is available with the name : panda_copy.jpg")
f1.close()

# Output:
# New image is available with the name : panda_copy.jpg




