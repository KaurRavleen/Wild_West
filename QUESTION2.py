#QUESTION 2: IMPLEMENT THE FOLLOWING TO THE SINGLY LINKED LIST.
#POP FUNCTION(REMOVE THE NODE FROM THE END OF THE LIST AND RETURN THE LIST).

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def pop(self):
        if self.head==None:
            return "UNDEFINED"
        remove=Node
        if self.head ==self.tail:
            self.head=None
            self.tail=None
        else:
            current=self.head
            while not(current.next==self.tail):
                current=current.next
            remove=current.next
            current.next=None
            self.tail=current
        self.length-=1
        return remove                 
