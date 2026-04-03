n =int(input("Enter the size of array:"))
arr = []
for i in range(n):
   val = int(input("Enter the value:"))
   arr.append(val)
sum = 0
print (arr)
for i in range(n):
   if i+1 in range(n):
      sum += abs(arr[i] - arr[i+1])  
print(sum)

# Output:
# Enter the size of array:5
# Enter the value:1
# Enter the value:2
# Enter the value:3
# Enter the value:4
# Enter the value:5
# [1, 2, 3, 4, 5]
# 4

