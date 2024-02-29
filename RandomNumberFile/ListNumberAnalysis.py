# Author: Weijia Fang
# Title: List Number Analysis
# Completion Date: Feb 2019

print("The following numbers were read from the random.txt file: ")

#Open the file 
f = open('random.txt','r')
lines = f.readlines()

#Convert to list
aList = []  #Create a empty list
for line in lines:
    num = int(line)
    aList.append(num)
    print(num)

#Output the result
print ("The lowest number in the list is:",min(aList))
print ("The highest number in the list is:",max(aList))
print ("The total of the numbers is:",sum(aList))
print ("The average of the numbers in the list is:",round(sum(aList)/len(aList),1))

#Close the file
f.close()
