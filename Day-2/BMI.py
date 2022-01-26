# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_f = float(height)
weight_f = float(weight)
Body_massindex = weight_f/height_f**2
print(int(Body_massindex))