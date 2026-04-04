#rearrange positive negative numbers in array
a = [-1, 2, -3, 4, 5, -6]
b = []
c = []
for i in a:
    if i > 0:
        b.append(i)
    else:
        c.append(i)
d = []
for i in range(len(b)):
    d.append(c[i])
    d.append(b[i])
print(d)

# Output:
# [-1, 2, -3, 4, -6, 5]


 