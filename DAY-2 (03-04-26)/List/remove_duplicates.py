arr = [1, 2, 3, 2, 5]
newlist = []
for i in arr:
    if i not in newlist:
        newlist.append(i)

print("input:", arr)
print("output:", newlist) 

# Output:
# input: [1, 2, 3, 2, 5]
# output: [1, 2, 3, 5]
