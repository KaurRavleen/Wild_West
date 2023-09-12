#QUESTION 6: IMPLEMENT THE FOLLOWING IN THE SINGLY LINKED LIST.
# SET FUNCTION(SHOULD ACCEPT AN INEX AND A VALUE AND UPDATE THE VLUE OF NODE IN LIST).

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def push(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
        else:
            self.tail.next=node
        self.tail=node 
        self.length+=1
        return "SUCCESS"       

    def set(self,index,value):
        if self.head is None:
            self.head=Node(value)
            self.tail=Node(value)
        else:
            current=self.head
            for i in range(index):
                current=current.next
                if current==None:           #reached end of the linkedlist
                    return False
            current.val=value               #otherwise set value
        return True        
