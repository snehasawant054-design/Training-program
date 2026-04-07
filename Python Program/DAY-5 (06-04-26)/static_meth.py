class Student:

    @staticmethod
    def get_personal_details(firstname,lastname):
        print("Your personal details : ", firstname, lastname)

    @staticmethod
    def contact_details(mobile_no,roll_no):
        print("Your contact details : ", mobile_no, roll_no)


Student.get_personal_details("sneha","sawant")
Student.contact_details(9876543210,1)

# Output:
# Your personal details :  sneha sawant
# Your contact details :  9876543210 1