print("Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate) ")
hours = input("Please provide your hours:",)
rate = input("Please provide your rate:",)

def computepay(hours, rate):

    try:
        if float(hours) > 40:
            overtime = float(rate)*(float(hours)-(float(hours)-40))+((float(hours)-40)*float(rate)*1.5)
            print("You earned overtime, your pay is", overtime)
            return overtime

        else:
            pay = float(rate)*float(hours)
            print("Your pay is", pay)
            return pay

    except:
        print("Error, please enter numeric input")



result = computepay(hours,rate) #solution to exercise

print("Test Pay", result )
