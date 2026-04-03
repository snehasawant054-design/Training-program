A = [1,2,3]
B = [2,3,4]
C = [3,4,5]
D = []
for x in A:
    if x in B and x in C:
        D.append(x)

print(D) 

# Output:
# [3]