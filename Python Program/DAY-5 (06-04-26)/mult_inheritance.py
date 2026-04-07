class subjMarks:
    math = int(input("Enter marks in Math : "))
    DE = int(input("Enter marks in DE : "))
    C = int(input("Enter marks in C : "))
    english = int(input("Enter marks in English : "))

class PractMarks:
    cprac = int(input("Enter marks in C prac : "))

class Result(subjMarks, PractMarks):
    def total(self):
        if self.math >= 40 and self.DE >= 40 and self.C >= 40 and self.english >= 40 and self.cprac >= 40:
            print("Pass")
        else:
            print("Fail")

obj = Result()
obj.total()

# Output:
# Enter marks in Math : 45
# Enter marks in DE : 56
# Enter marks in C : 67
# Enter marks in English : 78
# Enter marks in C prac : 89
# Pass