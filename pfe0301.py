print("Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.")
hours=input("Enter your hours:",)
rate = input("Enter your rate:",)
if float(hours) > 40:
    overtime = float(rate)*(float(hours)-(float(hours)-40))+((float(hours)-40)*float(rate)*1.5)
    print("You earned overtime, your pay is", overtime)
else:
    pay = float(rate)*float(hours)
    print("Your pay is", pay)
