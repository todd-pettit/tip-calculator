print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
num_of_people = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_multiplier = tip_percentage / 100
per_person_total = "{:.2f}".format(round((total_bill + (total_bill * tip_multiplier)) / num_of_people, 2))
print(f"Each person should pay: ${per_person_total}")
