# Author: Weijia Fang
# Title: Popular Names
# Completion Date: Feb 2019

#Open the file contains girls name and make the names into a list
fGirl = open("GirlNames.txt", "r")
lGirl = []
for line in fGirl.readlines():
    line = line.strip()
    lGirl.append(str(line))

#Close the file    
fGirl.close()

#Open the file contains boys name and make the names into a list
fBoy = open("BoyNames.txt", "r")
lBoy = []
for line in fBoy.readlines():
    line = line.strip()
    lBoy.append(str(line))

#Close the file  
fBoy.close()

print("Enter a name to see if it is a popular girls or boys name.\n")

#Ask for input value
AName = input('Enter a name to check, or "stop" to stop: ')

#A while loop to search for the input value in lists and output the result according to different situation
while AName != "stop":
    IsPopularGirl = (AName in lGirl);

    if IsPopularGirl == True:
        GirlRank = lGirl.index(AName, 0)
        print(AName + " is a popular girls name and is ranked: " + str(GirlRank + 1))
    else:
        print(AName + " is not a popular girls name.")

    IsPopularBoy = (AName in lBoy);

    if IsPopularBoy == True:
        BoyRank = lBoy.index(AName, 0)
        print(AName + " is a popular boys name and is ranked: " + str(BoyRank + 1))
    else:
        print(AName + " is not a popular boys name.")
    
    AName = input('\nEnter a name to check, or "stop" to stop: ')
