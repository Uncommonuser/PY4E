print("Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. ")
hours = input("Please provide your hours:",)
rate = input("Please provide your rate:",)
try:
    if float(hours) > 40:
        overtime = float(rate)*(float(hours)-(float(hours)-40))+((float(hours)-40)*float(rate)*1.5)
        print("You earned overtime, your pay is", overtime)
    else:
        pay = float(rate)*float(hours)
        print("Your pay is", pay)
except:
    print("Error, please enter numeric input")
