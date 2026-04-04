print('Subjects Marks:')
phy = 50
chem = 60
math = 70
print("Physics={} Chemistry={} Maths={}".format(phy,chem,math))
print("Physics={0} Chemistry={1} Maths={2}".format(chem,phy,math))
print("Physics={x} Chemistry={y} Maths={z}".format(x=phy,y=chem,z=math))

total = phy+chem+math
print("Total Marks={}".format(total))
print("Roll No=", "7".zfill(4))

# Output:
# Subjects Marks:
# Physics=50 Chemistry=60 Maths=70
# Physics=60 Chemistry=50 Maths=70
# Physics=50 Chemistry=60 Maths=70
# Total Marks=180
# Roll No= 0007



