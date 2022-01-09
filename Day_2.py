print("Welcome to the Tip Calculator")
bill=float(input("What was the total bill: "))
tip=int(input("What percentage tip would you like to give? 10 12 15  "))
people=int(input("How many people to split the bill: "))
bill_with_tip=(tip/100 * bill +bill)/people
final_bill=round(bill_with_tip,2)
print("Every person should pay: ",final_bill)
val = type(123_456_789)
print(val)