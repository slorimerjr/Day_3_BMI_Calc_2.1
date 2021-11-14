# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(float(weight / height**2), 1)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif 25 > bmi > 18.5:
  print(f"Your BMI is {bmi}, you are normal weight.")
elif 30 > bmi > 25:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 35 > bmi > 30:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")



