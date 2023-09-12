#QUESTION1: IMPLEMENT THE FOLLOWING TO A SINGLY LINKED LIST:
#PUSH FUNCTION (ADD THE NODE AT THE END OF THE LINKED LIST).

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


            
