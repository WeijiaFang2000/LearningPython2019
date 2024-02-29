# Author: Weijia Fang
# Title: Windchill
# Completion Date: March 2019

#A function that ask for input
def get_input():
    global temperature
    global windspeed
    temperature = float(input("Enter the Fahrenheit temperature: "))
    windspeed = float(input("Enter the wind speed: "))

#A function to calculate the windchill and print the result
def calculate_windchill(temperature,windspeed):
    windchill = 35.74 + 0.6215 * temperature - 35.75 * windspeed**0.16 + 0.4275 * temperature * windspeed**0.16
    print ("The windchill is:",round(windchill,1),'\n')
    
#Main program
print("This program calculates the windchill from the fahrenheit temperature and the wind speed.",'\n')
#Use these 2 functions above
get_input()
calculate_windchill(temperature,windspeed)

#Set a condition and ask whether to continue
condition = input('Would you like to calculate another windchill? Enter "y" or "n": ')
if condition == 'y':
    get_input()
    calculate_windchill(temperature,windspeed)
    condition = input('Would you like to calculate another windchill? Enter "y" or "n":')

