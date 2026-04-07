class College:                                  
    def college_name(self):
        print("Your College Name : YBIT")

class Student(College):
    def student_name(self):
        print("Your Student Name : Varsha")

obj1 = Student()
obj1.college_name()
obj1.student_name()

# Output:
# Your College Name : YBIT
# Your Student Name : sneha