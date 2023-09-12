#QUESTION 3: IMPLEMENT THE FOLLOWING ON THE SINGLY LINKED LIST.
#GET FUNCTION (SHOULD FIND NODE AT ANY SPECIFIC INDEX.)

class Node:
    def __init__(self,val):
        self.val=val
        self.next=next

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

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        current=self.head
        for i in range(index):
            current=current.next        #index starts from 0
        return current            