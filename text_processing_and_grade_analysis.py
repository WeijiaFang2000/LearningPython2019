# Author: Weijia Fang
# Title: text_processing_and_grade_analysis.py
# Completion Date: Sep 2019

def removePunctuation(txt):
    if not isinstance(txt,str): #Determine if the input is a string or not. If not, return None.
        return None

    s = '' #Initialize a string
    for i in txt: 
        if i.isalpha() == True: #Determine if the input is a alphabet letter or not. If yes, add to the list.
            s = s + i
        else:
            s = s + ' ' #If the input is not a alphabet letter, replace it with a blank
    return s

def studentGrades(gradeList):
    if not isinstance(gradeList,list): #Determine if the input is a list or not. If not return None.
        return None

    avggrades = [] #Initialize a list
    for i in range(1,len(gradeList)): #The loop starts from the second element(index =1)
        sum = 0 #Initialize the sum
        for j in range(1,len(gradeList[i])): #The second loop starts from the second element (index =1)
            sum = sum + gradeList[i][j]     #Calculate the total
        avg = int(sum/(len(gradeList[i])-1)) #Calculate the average grade
        avggrades.append(avg) #Add the result to the list
    return avggrades

grades = [['Student', 'Quiz 1', 'Quiz 2', 'Quiz 3'],
['John', 100, 90, 80],
['McVay', 88, 99, 111],
['Rita', 45, 56, 67],
['Ketan', 59, 61, 67],
['Saranya', 73, 79, 83],
['Min', 89, 97, 101]]

print(studentGrades(grades))