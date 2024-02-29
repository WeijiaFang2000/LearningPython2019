# Author: Weijia Fang
# Title: linked_list_queue.py
# Completion Date: Oct 2019

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return f'Head:{self.head}\nTail:{self.tail}\nQueue:{out}'

    __repr__=__str__

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def enqueue(self, x):
        new_node = Node(x)
        #When the queue is empty
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            self.count += 1
            return

        #When the queue contains only 1 item
        if self.head == self.tail:
            self.head.next = new_node
            self.tail = new_node
            self.count += 1
            return

        #When the queue contains two or more items
        self.tail.next = new_node #Find the tail of the original queue and insert the new_node to the tail
        self.tail = new_node #Let new_node be the tail
        self.count += 1

    def dequeue(self):
        #When the queue is empty
        if self.count == 0:
            return 'Queue is empty'

        #When the queue only contains 1 item
        if self.count == 1:
            result = self.head.value
            self.head = None
            self.tail = None
            self.count -= 1
            return result

        #When the queue contains two or more items
        result = self.head.value
        self.head = self.head.next
        self.count -= 1
        return result

    def __len__(self):
        return self.count

    def reverse(self): 
        if self.count == 0: #Base case of the recursion
            return
        head_value = self.head.value #head_value temperaily store the value of self.head
        self.dequeue() #Remove the head so we left with the queue without the head
        self.reverse() #Recursion
        self.enqueue(head_value) #Add the head_value to the tail of the queue