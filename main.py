#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
totalbill = input("What was the total bill? ")
totalbill_int = int(totalbill)
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_int = int(tip)
people = input("How many people to split the bill? ")
people_int = int(people)
new_tip_int = ((tip_int / 100) * totalbill_int)
eachperson_shouldpay = ((totalbill_int + new_tip_int) / people_int)
# new_eachperson_shouldpay = print(round(eachperson_shouldpay,2))
final_amount = "{:.2f}".format(eachperson_shouldpay)
print(f"Each person should pay: ${final_amount}")