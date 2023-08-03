# program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. 
# e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# BMI = weight (kg)/ height^2 (m^2)

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# Using the exponent operator **
bmi = weight / height ** 2
# or using multiplication and PEMDAS
bmi = weight / (height * height)

print("BMI: " + str(int(bmi)))