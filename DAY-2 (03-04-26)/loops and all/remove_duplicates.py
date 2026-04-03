#remove dublicates from string using for loop
name = "sawant"
new_name = ""
for i in name:
    if i not in new_name:
        new_name += i
print(name)
print(new_name)


# Output:
# sawant
# sawnt


