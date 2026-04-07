
class Principal:  
    def role(self):  
        print("I am managing all activity of college")  
  
class Dean:  
    def role(self):  
        print('Dean= I am decision taking person')  
          
class Hod:  
    def role(self):  
        print('Hod= I have responsibility of Teachers and Students')         
class Faculty:  
    def response(self):  
        print('Faculty= I have to complete syllabus successfully')  

def  func(obj):                                                      
    obj.role()                                                      
campus=[Principal(),Dean(),Hod(),Faculty()]   
for obj in campus:                                                 
    func(obj)

# Output:
# I am managing all activity of college
# Dean= I am decision taking person
# Hod= I have responsibility of Teachers and Students
# AttributeError: 'Faculty' object has no attribute 'role'