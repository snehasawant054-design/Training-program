# class Father:
#     def _init_(self):
#         print("Father := I am already at breakfast table")

# class Child(Father):
#     def _init_(self):
#         print("Child := I will be late for the breakfast")
#         super()._init_()

# obj = Child()

# Output:
# Child := I will be late for the breakfast
# Father := I am already at breakfast table

class Arithmetic:
    def _init_(self):
        print("There is no argument")
    def _init_(self,a):
        print("Passing 1 argument")
    def _init_(self,a,b):
        print("Passing 2 argument")
   
obj = Arithmetic()
obj.add(10)
obj.add(10,20)

# Output:
# There is no argument
# Passing 1 argument
# Passing 2 argument