#find majurity element in array
a = [3, 3, 4, 2, 4, 4, 2, 4, 4]
n = len(a)
for num in a:
    if a.count(num) > n / 2:
        print("Majority element is:", num)
        break
else:
    print("No majority element")

    # Output:
    # Majority element is: 4

