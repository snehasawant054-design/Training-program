#accept working day 

day = input("Enter the day: ")
if day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print("It's a working day.")
else:
    print("It's not a working day.")

    # Output1:
    # Enter the day of the week: Monday
    # It's a working day.
    # Output2:
    # Enter the day of the week: Saturday
    # It's not a working day.