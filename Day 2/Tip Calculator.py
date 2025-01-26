print("Welcome to the tip calculator")

bill_without_tip = float(input("What is your total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12 or 15? "))
group_size = int(input("How many people to split the bill? "))

total_bill = bill_without_tip * (100 + tip_percentage)/100

print(f"\nEach person should pay: ${total_bill/group_size:.2f}")