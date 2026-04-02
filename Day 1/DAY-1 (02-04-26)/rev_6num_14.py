num = 123456
a = num % 10
num = num // 10
print(num)
b = num % 10
num = num // 10
print(num)
c = num % 10
num = num // 10
print(num)
d = num % 10
num = num // 10
print(num)
e = num % 10
num = num // 10
print(num)
f = num % 10
rev = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f
print("Reverse number =", rev)

# Output:
# 12345
# 1234
# 123
# 12
# 1
# Reverse number = 654321