# Author: Weijia Fang
# Title: Falling Distance
# Completion Date: Feb 2019

#a def for calculation
def falling_distance(time):
    gravity = 9.8
    distance = 0.5*9.8*time*time
    return distance

print("This program tells you how far an object will fall in a number of seconds.")

#Ask for input
falltime = int(input("Enter the falling time in seconds: "))

#A while loop use the def that set up before to calculate, and output the result
while (falltime >= 0):
    falleddistance = round(falling_distance(falltime),1)
    print ("The distance the object will fall in",str(falltime),"seconds, is:",str(falleddistance),"meters.","\n")

    falltime = int(input("Enter the falling time in seconds: ")) #Ask for another input to enter the loop again
    
