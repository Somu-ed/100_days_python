#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the Tip Calculator Project")
bill = float(input("Enter the bill amount: $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15 percent? : "))
people = int(input("How many people to split the bill with? : "))

tip /= 100
total_tip = bill * tip
total_bill = bill + total_tip
bill_per_people = total_bill / people
rounded_amount = round(bill_per_people, 2)

print(f"Each person has to pay: ${rounded_amount}")