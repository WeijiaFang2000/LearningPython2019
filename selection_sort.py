# Author: Weijia Fang
# Title: selection_sort.py
# Completion Date: Nov 2019

def selectionSort(numList):
    '''
        Takes a list and returns 2 values
        1st returned value: a dictionary with the state of the list after each complete pass of selection sort
        2nd returned value: the sorted list

        >>> selectionSort([9,3,5,4,1,78,67])
        ({1: [9, 3, 5, 4, 1, 78, 67], 2: [1, 3, 5, 4, 9, 78, 67], 3: [1, 3, 5, 4, 9, 78, 67], 4: [1, 3, 4, 5, 9, 78, 67], 5: [1, 3, 4, 5, 9, 78, 67], 6: [1, 3, 4, 5, 9, 78, 67], 7: [1, 3, 4, 5, 9, 67, 78]}, [1, 3, 4, 5, 9, 67, 78])
    '''
    result = {} #Create a dict
    result_numList = numList.copy() #Use copy function to produce a new numList 
    result[1] = numList #The first value in the dict should be the original numList
    for i in range(0,len(result_numList)-1): 
        min = i
        for j in range(i+1,len(result_numList)): #Find the index of the minimum value
            if result_numList[j] < result_numList[min]:
                min = j
        #Swap
        temp = result_numList[i]
        result_numList[i] = result_numList[min]
        result_numList[min] = temp

        result[i+2] = result_numList.copy() #Put every result of loop into the dict
    return result,result_numList 