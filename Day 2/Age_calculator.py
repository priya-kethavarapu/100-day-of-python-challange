# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
remaining_years = 90 - int(age)
months = remaining_years * 12
weeks = 52 * remaining_years
days = remaining_years * 365
print(f"You have {days} days, {weeks} weeks, and {months} months left.")