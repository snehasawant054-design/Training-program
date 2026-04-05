with open("with.txt", "w") as f:
    f.write("sneha\n")
    f.write("paras\n")
    f.write("sawant\n")
    f.write("sawal\n")
    print("f.closed:",f.closed)
print("f.closed:",f.closed)

# Output:
# f.closed: False
# f.closed: True
