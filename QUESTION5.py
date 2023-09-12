#QUESTION 5: IMPLEMENT THE FOLLOWING THE IN SINGLY LINKED LIST.
#ROTATE FUNCTION (SHOULD ROTATE AALL THE NODES IN LIST BY SOME NUMBER PASSED IN).

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

    def rotate(self,number):
        index=(number + self.length) if number <0 else number
        if index<0 or index>=self.length:
            return None
        if index==0:
            return "NO ROTATION"
        prevNode= self.head
        for i in range(index-1):
            prevNode=prevNode.next
            if prevNode==None:
                return 'NO ROTATION'
        self.tail.next=self.head
        self.head=prevNode.next
        self.tail= prevNode
        prevNode.next=None
        return "SUCCESS"
            