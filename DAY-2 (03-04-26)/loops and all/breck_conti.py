# for i in range(1, 5):
#     if i == 3:
#         break
#     print(i)

# Output:
# 1
# 2

# for i in range(1, 5):
#     if i == 3:
#         continue
#     print(i)

# Output:
# 1
# 2
# 4

# for i in range(1, 6):
#     if i == 3:
#        continue
#     print(i)

# Output:
# 1
# 2
# 4
# 5

# for i in range(5,0,-1):
#     if i == 3:
#        continue
#     print(i)

# Output:
# 5
# 4
# 2
# 1

for i,j in zip(range(1,6), range(5,0,-1)):
    if i == 3 and j == 3:
       continue
    print(i," ",j)

# Output:
# 1   5
# 2   4
# 4   2
# 5   1



