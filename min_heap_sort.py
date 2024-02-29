# Author: Weijia Fang
# Title: min_heap_sort.py
# Completion Date: Nov 2019

class MinHeap:
    def __init__(self):
        self.heap=[]
      

    def __str__(self):
    	return f'{self.heap}'

    __repr__=__str__


    def parent(self,index):
        if index > len(self.heap) or index <= 1: #Dealing with situation when the index is greater than the length of the binary heap and less than or equal to 1
            return None
        return self.heap[index//2-1] 

    def leftChild(self,index):
        if index > len(self.heap) or index < 1: #Dealing with situation when the index is greater than the length of the binary heap, or, the index is less than 1
            return None
        if index*2 > len(self.heap): #Dealing with situation when there is no left child
            return None
        return self.heap[index*2-1]

    def rightChild(self,index):
        if index > len(self.heap) or index < 1: 
            return None
        if index*2+1 > len(self.heap): #Dealing with situation when there is no right child
            return None
        return self.heap[index*2]

    def __len__(self):
        return len(self.heap)
       
    def insert(self,x):
        self.heap.append(x) #Add the value to the list
        i = len(self.heap)
        #While the parent is not none and the parent is greater than x, exchange the last item with the parent
        while self.parent(i) != None and self.parent(i) > x:
            self.heap[i-1] = self.parent(i)
            self.heap[i//2-1] = x
            i = i//2 #Next loop start from the parent of the current item


    @property
    def deleteMin(self):
        if len(self)==0:
            return None        
        elif len(self)==1:
            out=self.heap[0]
            self.heap=[]
            return out

        removed_value = self.heap[0] #a temp variable to store the removed value and return it at the end
        self.heap[0] = self.heap[-1] #Put the last item in the list to the root of the binary heap
        self.heap = self.heap[:len(self.heap)-1] #Remove the last item from the list

        i = 1
        while i*2 <= len(self.heap):
            #If right child does not exist or left child is less than or equal to the right child
            if self.rightChild(i) == None or self.heap[i*2-1] <= self.heap[i*2+1-1]: 
                if self.heap[i-1] > self.heap[i*2-1]: #Compare the parent with the left child. If the parent is greater, exchange them
                    temp_variable = self.heap[i-1]
                    self.heap[i-1] = self.heap[i*2-1]
                    self.heap[i*2-1] = temp_variable
                i = i*2
            else: #If the right child is greater than the left child
                if self.heap[i-1] > self.heap[i*2+1-1]: #Compare the parent with the right child. If parent is greater, exchange them
                    temp_variable = self.heap[i-1]
                    self.heap[i-1] = self.heap[i*2+1-1]
                    self.heap[i*2+1-1] = temp_variable
                i = i*2+1
        return removed_value


def heapSort(numList):
    '''
       >>> heapSort([9,7,4,1,2,4,8,7,0,-1])
       [-1, 0, 1, 2, 4, 4, 7, 7, 8, 9]
    '''
    sort_heap = MinHeap()
    #Insert the values in the numList to the heap
    for i in numList:
        sort_heap.insert(i)
    temp = [] #A temp list to return the final sorted list

    #If sort_heap is not 0, it means it is a min heap, so its root value is the minimum
    #Delete the minimim in the heap and append it to the temp list
    while len(sort_heap) != 0:
        min_value = sort_heap.deleteMin
        temp.append(min_value)
    return temp