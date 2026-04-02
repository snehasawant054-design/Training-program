num = 123
a = num %10
print(a) #3
num = num // 10
print(num) #12
b = num % 10
print(b) #2
c = num // 10
print(c) #1
rev = a*100+b*10+c*1
print(rev) #321

# Output:
# 3
# 12
# 2
# 1
# 321