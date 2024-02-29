# Author: Weijia Fang
# Title: ordered_linked_list.py
# Completion Date: Oct 2019

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class OrderedLinkedList:
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
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__

    def isEmpty(self):
        return self.head == None

    def __len__(self):
        return self.count


    def add(self, value):
        new_node = Node(value)
        #When the linked list is empty
        if self.head == None and self.tail == None: #Determine if the linked list is empty
            self.head = new_node
            self.tail = new_node
            self.count += 1
            return

        #When the 1st node's value larger than the input value, make the new node be the head
        if self.head.value > value:
            new_node.next = self.head
            self.head = new_node
            self.count += 1
            return

        #Find the 1st node that is larger than the input value after the head
        current = self.head
        while current.next:
            if current.next.value < new_node.value:
                current = current.next
            else:
                break #Found the first hnode that is larger or equal to the input value

        if current.next == None: #Does not find that value until the end of the linked list, let the new node be the tail of linked list
            current.next = new_node 
            self.tail = new_node
        else: #Does find but that value is not the tail, we insert the new node after the current node
            new_node.next = current.next
            current.next = new_node
        self.count += 1


    def pop(self):
        #When the linked list is empty
        if self.head == None and self.tail == None:
            return None

        #When the linked list contain only one item
        if self.head.next == None:
            self.count -= 1
            result = self.tail.value
            self.head = None
            self.tail = None
            return result

        #When the linked list contain two or more items
        current = self.head
        while current.next.next: #Continue the loop if the second next is not None
            current = current.next 
            
        result = current.next.value
        current.next = None
        self.tail = current
        self.count -= 1
        return result


    def remDuplicates(self):
        #When the linked list contain two or more nodes
        current = self.head
        while current.next: #When current.next is equal to None, continue the loop
            if current.value == current.next.value: #Determine the current value is equal to the next value after current
                current.next = current.next.next #Removing the duplicated value
                if current.next == None: #If reach the end of the linked list, let self.tail be current
                    self.tail = current
                self.count -= 1
            else: #Let current equal to the next node
                current =current.next