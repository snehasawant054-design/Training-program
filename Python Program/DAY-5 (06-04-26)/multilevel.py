class College:                                  
    def college_name(self):                     
        print("Your College Name : YBIT")

class Student(College):                         
    def student_name(self):                     
        print("Your Student Name : Varsha")

class Exam(Student):                           
    def subject(self):                          
        print("Subject 1 : Python")
        print("Subject 2 : Java")
        print("Subject 3 : C++")

obj1 = Exam()                                  
obj1.college_name()                             
obj1.student_name()                             
obj1.subject()

# Output:
# Your College Name : YBIT
# Your Student Name : sneha
# Subject 1 : Python
# Subject 2 : Java
# Subject 3 : C++