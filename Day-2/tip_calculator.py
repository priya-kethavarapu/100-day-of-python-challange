#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("Total bill from the user? $"))
tip = int(input("Percentage of tip? 10, 12 or any? "))
splits = int(input("Number of splits? "))
tip_amount = bill * tip / 100
total_bill = bill + tip_amount
each_split = total_bill/splits
final_amount = round(each_split , 2)
final_amount = "{:.2f}".format(final_amount)
print(f"Each person should pay: ${final_amount}")