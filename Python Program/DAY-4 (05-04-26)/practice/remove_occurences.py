
# list = [1,2,2,3,4,2]
# while 2 in list:
#     list.remove(2)
# print(list)

# Output:
# [1, 3, 4]

list = [1,2,2,3,4,2]
rep = {}
for item in list:
    rep[item] = rep.get(item, 0) + 1
result = []
for item in list:
    if rep[item] == 1:
        result.append(item)
print("Original List:", list)
print("After removing repeated numbers:", result)

# Output:
# Original List: [1, 2, 2, 3, 4, 2]
# After removing repeated numbers: [1, 3, 4]






