# Author: Weijia Fang
# Title: Random Number File Reader
# Completion Date: Feb 2019

#This program requires to run the program for assignment 6 first
#These two programs and random.txt should under the same folder

print("The following numbers were read from the random.txt file: ")

#Open the file
f = open('random.txt','r')
lines = f.readlines()

#A loop to record numbers themselves and the number of numbers
#Add numbers to get the total
total = 0
count = 0
for line in lines:
    num = int(line)
    print(num)
    count += 1
    total = total + num

#Output the result
print ("The total of the numbers is:",total)
print ("The file contained",count-1,"numbers.") #dedection end of line

#Close the file
f.close()
