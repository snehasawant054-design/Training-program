mylist = [44,22,77,0,9,88]
newlist = mylist
print(id(mylist))
print(id(newlist))
mylist[0] = "sneha"
print(mylist)
print(newlist)

# Output:
# 1670871092992
# 1670871092992
# ['sneha', 22, 77, 0, 9, 88]
# ['sneha', 22, 77, 0, 9, 88]

