#QUESTION 4: IMPLEMENT THE FOLLOWING ON THE SINGLY LINKED LIST.
#INSERT FUNCTION(SHOULD INSERT A NODE AT A SPECIFIC INDEX IN THE LIST AND RETURN TRUE IF THE INDEX IS VALID ELSE FALSE).

from msilib.schema import SelfReg


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

    def insert(self,index,data):
        newNode=Node(data)
        if index<0 or index>self.length:
            return False
        if self.head is None:
            self.head=newNode
        else:
            self.tail=newNode
        if index==0:
            newNode.next=self.head
            self.head=newNode
        elif index==1:
            newNode.next=self.head.next
            self.head.next=newNode
        elif index==self.length:
            self.tail.next=newNode
            newNode.next=None
            self.tail=newNode
        else:
            tmp=self.head
            inx=0
            while inx<index-1:
                tmp=tmp.next
                inx+=1
            next=tmp.next
            tmp.next=newNode
            newNode.next=next
        self.length+=1
        return True                              
