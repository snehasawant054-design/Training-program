# Simple for loop example
names = [4, 2, 5, 6, 8, 2]
for i in names:
    print(i)

# Output:
# 4
# 2
# 5
# 6
# 8
# 2

# For loop with break condition
print("\nFor loop with break at 3:")
for i in range(1, 5):
    if i == 3:
        break
    print(i)
