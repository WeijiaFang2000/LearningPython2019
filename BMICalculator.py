# Author: Weijia Fang
# Title: BMI Calculator
# Completion Date: Jan 2019

height = int(input("Enter your height in inches: " ))
weight = int(input("Enter your weight in pounds: " ))
BMI = weight * 703 /height**2
print ("Your BMI is: ",round(BMI,1))
if BMI < 18.5:
    print ("Your BMI indicates that you are underweight.")
elif BMI > 25:
    print ("Your BMI indicates that you are overweight.")
else:
    print ("Your BMI indicates that you are optimal weight.")
