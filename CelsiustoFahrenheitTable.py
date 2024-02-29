# Author: Weijia Fang
# Title: Celsius to Fahrenheit Table
# Completion Date: Feb 2019

input_temperature = int(input("Enter the number of celsius temperatures to display: "))
print ("Celsius   Fahrenheit")
for i in range(0,input_temperature+1):
    C = i
    F = 9/5*C+32
    print ("{:<2}".format(C), "       {0:>.1f}".format(F))
