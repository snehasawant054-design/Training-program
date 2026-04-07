
class New:  
    a = 10                          

    def _init_(self):
        self.b = "Varsha"         

obj1 = New()
obj2 = New()
obj3 = New()
obj1 = New()
obj2 = New()
obj3 = New()

print(obj1.a)
print(obj2.a)
print(obj3.a)

New.a = 50

print(obj1.a)
print(obj2.a)
print(obj3.a)

# Output:
# 10
# 10
# 10
# 50
# 50
# 50
