print("Welcome to the tip calculator")
bill = float(input("What is the total bill? €"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
no_of_people = int(input("How many people would split the bill? "))
tip_as_percent = tip / 100
bill_with_tip = bill * (1 + tip_as_percent)
bill_per_person = bill_with_tip / no_of_people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: €{final_amount}")
