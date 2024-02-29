# Author: Weijia Fang
# Title: Grade Average With Exceptions
# Completion Date: March 2019

#A function to calculate the average
def calculate_average(sum,count):
    average = sum/count
    return average

#Main program

#Set initial values
grade = 0
count = 0
sum = 0

#Determine the first input
try:
    grade = int(input("Enter a positive number to total or a negative number to calculate average: "))
    sum = sum+grade
    count += 1
except ValueError:
    print("What you entered was not a valid number. Try again.")

#A while loop to ask for input and deal with inputs according to different situation
while (grade >= 0):
    try:
        grade = int(input("Enter a positive number to total or a negative number to calculate average: "))
        if (grade>=0):
            count += 1
            sum = sum +grade
    except ValueError:
        print("What you entered was not a valid number. Try again.")
average = calculate_average(sum,count) #call the calculate_average function to get average

#Output the 
print ("The sum of the numbers is:",sum)
print ("The average of the numbers is: ",round(average,1))
