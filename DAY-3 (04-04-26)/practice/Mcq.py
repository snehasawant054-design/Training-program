# mydict = {}
# mydict[1] = 1
# mydict['1'] = 2
# mydict[1.0] = 4
# print(mydict)
# sum = 0
# for k in mydict:
#     sum += mydict[k]
# print(sum)

# Output:
# {1: 4, '1': 2}
# 6

# mydict = {}
# mydict[(1,2,4)] = 8
# mydict[(4,2,1)] = 10
# mydict[(1,2)] = 12
# print(mydict)
# sum = 0
# for k in mydict:
#     sum += mydict[k]
# print(sum)

# Output:
# {(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12}
# 30

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates['box']))

# Output:
# 2

# dict = {'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_],end="")

# Output:
# 96
# 98
# 97

# rec = {"name":"python","age":"20"}
# r = rec.copy()
# print(id(r) == id(rec))

# Output:
# False

# rec = {"name":"python","age":"20", "addr":"NJ","country":"USA"}
# id1 = id(rec)
# print(id(id1))
# del rec
# rec =  {"name":"python","age":"20", "addr":"NJ","country":"USA"}
# id2 = id(rec)
# print(id(id2))
# print(id1 == id2)

# Output:
# 1858175220752
# 1858175220720
# True





