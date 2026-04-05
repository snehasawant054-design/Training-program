
a = [5,7,8,3,7,8,9,2,3]
fre_ele = {}
count = 0
for i in a:
    fre_ele[i] = fre_ele.get(i, 0) + 1
    if fre_ele[i] >1:
        count += 1
print(count)

# Output:
# 3
       







 

