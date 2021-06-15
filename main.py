print("Welcome to the tip calculator")
bill = input("What was your total bill? ")
tip = input("What percentage tip would you like to give? 10, 12 or 15 ")
people = input("How many people are splitting the bill? ")

bill_int = int(bill)
tip_int = int(tip)
people_int = int(people)

percentage = tip_int / 100

total = (bill_int + percentage) / people_int

final = (round(total, 2))

print(f"Everyone should pay ${final}")
