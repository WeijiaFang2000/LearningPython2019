# Author: Weijia Fang
# Title: Grade Average
# Completion Date: Feb 2019

score = 0
numberofscore = 0
totalscore = 0
score = int(input("Enter a test score, -1 to get the average: "))
while (score >= 0):
    totalscore = totalscore + score
    numberofscore += 1
    score = int(input("Enter a test score, -1 to get the average: "))
if (numberofscore != 0):
    average = totalscore/numberofscore
    print ("The average for all the grades is: ",round(average,1))
else:
    print ("Nothing inputed.")
