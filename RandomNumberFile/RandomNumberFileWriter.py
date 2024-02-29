# Author: Weijia Fang
# Title: Random Number File Writer
# Completion Date: Feb 2019

import random

print("This program writes random numbers to the random.txt file.")

#Ask for how many numbers does the user want and output
totalnumber = int(input("How many numbers would you like to write: "))
print(totalnumber,"numbers were written to the random.txt file")

#Open the random number file
f = open('random.txt','w')

#For loop: generate the random number, convert it to string and write it in the file
for i in range(0,totalnumber+1):
    numbers = random.randint(1,500)
    convertedstr = str(numbers)
    f.write(convertedstr+'\n')

#Close the file
f.close()
