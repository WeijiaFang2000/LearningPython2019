# Author: Weijia Fang
# Title: generators_inf_filter_accum.py
# Completion Date: Dec 2019

def genInf(aList):
    '''
        >>> g = genInf([5,'a',2])
        >>> next(g)
        5
        >>> next(g)
        'a'
        >>> next(g)
        2
        >>> next(g)
        5
        >>> next(g)
        'a'
        >>> next(g)
        2
    '''
    i = 0 #Initialize the index to 0

    while True:
        yield aList[i] #yield the item which index is equal to i
        i += 1 #Index plus 1, go to the next item
        if i >= len(aList): #If the value of i exceeds the length of the given list, make i equal to 0 so that it start again
            i = 0

def genFilter(seq, fn):
    """ 
        >>> isEven = lambda x: x % 2 == 0 
        >>> list(genFilter(range(5), isEven)) 
        [0, 2, 4]
        >>> oddNum = (2*i-1 for i in range (10)) 
        >>> list(genFilter(oddNum, isEven)) 
        []
        >>> g = genFilter(range(1,11), isEven) 
        >>> next(g) 
        2
        >>> next(g) 
        4
        >>> next(g) 
        6
        >>> next(g) 
        8
        >>> next(g) 
        10
        >>> next(g) 
        Traceback (most recent call last):
        ...
        StopIteration
    """
    for item in seq: 
        if fn(item) == True: #Determine whether the fn is True or False, if True, return the item itself
            yield item

def genAccum(seq, fn):
    '''
        >>> add = lambda x, y: x + y
        >>> mul = lambda x, y: x * y
        >>> list(genAccum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], add))
        [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        >>> list(genAccum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], mul))
        [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    '''
    #Making sure seq is a list and it is not empty
    if not isinstance(seq,list) or len(seq) == 0:
        return 'Error input: seq must be a list and it cannot be empty.'

    for i in range(len(seq)):
        it = iter(seq[:i+1]) #Generate an iterable from index = 0 to index = i
        answer = next(it) #The first value
        for item in it: #Call fn to produce answer in to a list from index = 1 to index = i
            answer = fn(answer,item)
        yield answer