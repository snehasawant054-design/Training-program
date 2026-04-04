mylist=["sneha","paras","varsha","manasi",15,15.28,"sneha"]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:])
print(mylist[1:8:5])
print(mylist[:])
print(mylist[::-1])

# Output:
# ['sneha', 'paras', 'varsha', 'manasi', 15, 15.28, 'sneha']
# <class 'list'>
# sneha
# paras
# varsha
# sneha
# ['varsha', 'manasi', 15]
# ['sneha', 'paras', 'varsha', 'manasi', 15]
# ['paras', 'varsha', 'manasi', 15, 15.28, 'sneha']
# ['paras', 'sneha']
# ['sneha', 'paras', 'varsha', 'manasi', 15, 15.28, 'sneha']
# ['sneha', 15.28, 15, 'manasi', 'varsha', 'paras', 'sneha']
