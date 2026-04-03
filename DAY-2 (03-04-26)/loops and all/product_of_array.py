#product of array
a = [1,2,3,4]
b = []
for i in range(len(a)):
    product = 1
    for j in range(len(a)):
        if i != j:
            product *= a[j]
    b.append(product)
print(b)

# Output:
# [24, 12, 8, 6]
