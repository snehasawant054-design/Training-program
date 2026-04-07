# class rbi:
#     def home_loan(self):
#         print("Home Loan = 7.5")
#     def car_loan(self):
#         print("Car Loan = 8 %")

# class sbi(rbi):
#     def home_loan(self):
#         print("SBI Provide Home Loan = 6.5 %")      
#         super().home_loan()

# obj = sbi()
# obj.home_loan()

# Output:
# SBI Provide Home Loan = 6.5 %
# Home Loan = 7.5

class Arithmatic:  
    def add(self,a=None,b=None,c=None):  
        if a!=None and b!=None:
            print(a+b)
        elif a!=None and b!=None and c!=None:
            print(a+b+c)
        else:
            print("Enter Atleast 2 Argument")  
obj = Arithmatic()  
obj.add(10)  
obj.add(10,20)  
obj.add(1,2,3)

# Output:
# Enter Atleast 2 Argument
# 30
# 6