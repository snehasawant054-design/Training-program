#WAP to change calculation with respect to total amount 
Amount = int(input("Enter the amount: "))
print("100 notes: ", Amount//100)
print("50 notes: ", (Amount%100)//50)
print("20 notes: ", ((Amount%100)%50)//20)
print("10 notes: ", (((Amount%100)%50)%20)//10)
print("5 notes: ", ((((Amount%100)%50)%20)%10)//5)

