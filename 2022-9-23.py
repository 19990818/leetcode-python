
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.size=0
        self.list=None

    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        cur=self.list
        while index>0:
            cur=cur.next
            index-=1
        return cur.val

    def addAtHead(self, val: int) -> None:
        newL=ListNode(val)
        newL.next=self.list
        self.list=newL
        self.size+=1

    def addAtTail(self, val: int) -> None:
        cur=self.list
        self.size+=1
        if cur==None:
            self.list=ListNode(val)
            return
        
        while cur.next!=None:
            cur=cur.next
        cur.next=ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return
        if index<=0:
            self.addAtHead(val)
            return
        if index==self.size:
            self.addAtTail(val)
            return
        cur=self.list
        self.size+=1
        while index>1:
            index-=1
            cur=cur.next
        tempPost=cur.next
        newNode=ListNode(val)
        cur.next=newNode
        newNode.next=tempPost

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return
        cur=self.list
        self.size-=1
        if index==0:
            self.list=self.list.next
            return
        while index>1:
            index-=1
            cur=cur.next
        cur.next=cur.next.next