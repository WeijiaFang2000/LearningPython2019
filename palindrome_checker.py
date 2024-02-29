# Author: Weijia Fang
# Title: palindrome_checker.py
# Completion Date: Sep 2019

def isPalindrome(text):
    #If the input is not a string, return False
    if not isinstance(text,str): 
        return False

    lowertext = text.lower() #Make all strings to lower case

    onlyalphaandnumtxt = '' #Initialize a string that have alphabet letter and numbers
    #A for loop: when the letter in the string is alphabet letter or number, add to the new string(onlyalphaandnumtxt)
    for j in range(0,len(lowertext)): 
        if lowertext[j].isalnum() == True:
            onlyalphaandnumtxt = onlyalphaandnumtxt + lowertext[j]

    isPalindromeString = True #Initialize the boolean variable to True
    #A loop that compare the first letter with the last letter, and second letter with the last second letter...and so on. 
    #If unequal, it is not a palindrome, so return False
    for i in range(0,len(onlyalphaandnumtxt)): 
        if onlyalphaandnumtxt[i] != onlyalphaandnumtxt[len(onlyalphaandnumtxt)-1-i]:
            return False

    #If all equal/did not find unequal, it is a palindrome, so return True 
    return isPalindromeString