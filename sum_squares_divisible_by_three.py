# Author: Weijia Fang
# Title: sum_squares_divisible_by_three.py
# Completion Date: Aug 2019

def sumSquares(aList):
    if not isinstance(aList,list):
        return "error"

    sum = 0
    for i in range(0,len(aList)):
        if isinstance(aList[i],int) or isinstance((aList[i]),float):
            if aList[i] % 3 == 0:
                sum = sum + aList[i]*aList[i]
    return sum