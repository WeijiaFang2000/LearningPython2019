# Author: Weijia Fang
# Title: digit_sum_alternator.py
# Completion Date: Dec 2019

def digitSum(num):
    '''
        >>> digitSum(15)(555)
        True
        >>> digitSum(22)(2578)
        True
        >>> digitSum(258)(1011010101010)
        False
    ''' 
    #Making sure num is an int
    if not isinstance(num,int):
        return 'Error input: input must be a integer.'

    #A function that add the number of each digits together
    def add_digits(x):
        #Making sure x is an int
        if not isinstance(x,int):
            return 'Error input: input must be a integer.'

        if x%10 < 1: #Base case of recursion
            return x 
        else: 
            return x % 10 + add_digits(x//10) 
    
    #A function to compare the result from previous function and x
    #If equal, return True, otherwise return False
    def is_equal(x):
        #Making sure x is an int
        if not isinstance(x,int):
            return 'Error input: input must be a integer.'

        if add_digits(x) == num:
            return True
        else:
            return False

    return is_equal

def alternate(fn1, fn2):
    '''
        >>> def isEven(x):
        ...    return x % 2 == 0
        >>> ex1 = alternate(isEven, lambda x: x + 4)
        >>> ex1(5)
        [False, 6, False, 8, False]
        >>> ex2 = alternate(lambda x: x * 2, lambda x:x%5 if x<6 else x%2)
        >>> ex2(7)
        [2, 2, 6, 4, 10, 0, 14]
    '''
    #A function to determine whether to use fn1 or fn2
    def get_odd_even_list(n):
        #Making sure n is an int
        if not isinstance(n,int):
            return 'Error input: n must be a integer.'

        aList = [] #Create an empty list to receive values
        #A for loop:
        #For every even number, we should append it to fn1; for every odd number, we should append it to fn2
        for i in range(1, n+1):
            if not i % 2 == 0:
                aList.append(fn1(i))
            else:
                aList.append(fn2(i))
        return aList 
        
    return get_odd_even_list