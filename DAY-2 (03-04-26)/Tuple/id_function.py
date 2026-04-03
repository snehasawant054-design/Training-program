# init_tuple_a = 'a','b'
# init_tuple_b = ('a','b')
# print (init_tuple_a == init_tuple_b)

# Output:
# True

# init_tuple_a = '1','2'
# init_tuple_b = '3','4'
# print(init_tuple_a + init_tuple_b)

# Output:
# ('1', '2', '3', '4')

# init_tuple = (1,)*3
# init_tuple[0] = 2
# print(init_tuple)

# Output:
# TypeError: 'tuple' object does not support item assignment

# init_tuple = ((1, 2),) *7
# print(len(init_tuple[3:8]))

# Output:
# 4

A = [4,0,2,5,0,1]
B = [4,2,5,1,0,0]
# Move zeros to the last
for i in range(len(A)):
    if A[i] == 0:
        A.append(A.pop(i))
print(A)

# Output:
# [4, 2, 5, 1, 0, 0]
