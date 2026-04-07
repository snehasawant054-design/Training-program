class Student:
    def _init_(self, name, roll_no,mobile_no):
        self.name = name                                
        self.roll_no = roll_no
        self.mobile_no = mobile_no

    def display(self):                                 
        print(self.name,self.roll_no,self.mobile_no)                    

obj1 = Student("sneha", 1, 9876543210)
obj1.display()

# Output:
# sneha 1 9876543210

