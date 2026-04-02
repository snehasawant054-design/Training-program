p_amount = int(input("Enter principle Amount:"))
roi = int(input("Enter ROI:"))
time = int(input("Enter duration of loan amount:"))
si = p_amount*roi*time/100
print("simple intrest=",si)

# Output:
# Enter principle Amount:5000
# Enter ROI:200
# Enter duration of loan amount:3
# simple intrest= 30000.0