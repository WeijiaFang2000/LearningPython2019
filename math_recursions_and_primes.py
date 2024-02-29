# Author: Weijia Fang
# Title: math_recursions_and_primes.py
# Completion Date: Oct 2019


def mulBy(num):
    if isinstance(num,int) == False: #Make sure the input value is a integer, if not, return 'Error'
        return 'Error'
    if num < 0: #Make sure the input value is greater than 0, if not, return 'Error'
        return 'Error'
    if num == 0: #If input value = 0, return itself
        return num

    if num == 1 or num == 2: #The base case of the recursion is the num == 1 or 2
        return num #When it equal to 1 or 2, stop the recursion
    else:
        return num*mulBy(num-2) #If it does not equal to 1 or 2, keep -2
    

def flat(aList):
    #Determine if the list is empty or not, if yes, return []
    if aList == []:
        return []
    #If the first item in the list is a list, seperate this list to two lists. 
    #First list only contains the first item, and the second list contains all remaining items.
    #Use recursion to find the flattened lists respectively, and add the results together
    if isinstance(aList[0], list):
        return flat(aList[0])+flat(aList[1:])
    else: #Another situation: use a list that contains the first item, and use recursion to flat the remaining items
        return aList[:1]+flat(aList[1:])


def isPrime(num,start=2):
    #Determine if num is an integer or not, if false, return Error
    if isinstance(num,int) == False:
        return 'Error'
    #If num is less than 2, num is not a prime number because it can only have 1 factor
    if num < 2:
        return False
    
    #Under the situation that factor*factor is less than num 
    if start*start <= num:
        if num%start == 0: #If num can divide the factor without remainder, it is not a prime number
            return False
        else: #If has remainder after the division, use recursion to add 1 to the factor
            return isPrime(num,start+1)
    #Under the situation that the factor is greater or eqaul to num
    else:
        return True

for i in range(1,101):
    print(str(i),"is a prime: " + str(isPrime(1)))

def countPrimes(num):
    #Determine if the num is an ingeter or not, if not, return 'Error'
    if isinstance(num,int) == False:
        return 'Error'
    #If num is less than 0, return 'Error'
    if num < 0:
        return 'Error'
    #If number is equal to 0, return 0
    if num == 0:
        return 0

    #Determine the num itself is a prime number or not, if yes, add 1 and use recursion to call the function with num-1
    if isPrime(num) == True:
        return 1 + countPrimes(num-1)
    else: #If no, use recursion to call the function with num -1
        return countPrimes(num-1)