
from ast import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode(0)
        temp=res
        while list1 is not None or list2 is not None:
            if list2 is None or (list1 is not None and list1.val<=list2.val):
                temp.next=list1
                list1=list1.next
            else:
                temp.next=list2
                list2=list2.next
            temp=temp.next
        return res.next
    
    
    
class Solution:
    class edge():
        def __init__(self,x,y,dis) -> None:
            self.x=x
            self.y=y
            self.dis=dis
    def find(self,a,parent):
        while a!=parent[a]:
            a=parent[a]
        return parent[a]
    def merge(self,e,parent,dis):
        rootx=self.find(e.x,parent)
        rooty=self.find(e.y,parent)
        if rootx==rooty:
            return 0
        parent[rooty]=rootx
        dis[rootx]+=dis[rooty]+e.dis
        return dis[rootx]
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        parent,dis=[0 for _ in range(0,n)],[0 for _ in range(0,n)]
        edges=[]
        for i in range(0,len(points)):
            parent[i]=i
            for j in range(i+1,len(points)):
                edges.append(self.edge(i,j,abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])))
        edges=sorted(edges,key=lambda x:x.dis)
        cnt=0
        for e in edges:
            temp=self.merge(e,parent,dis)
            if temp!=0:
                cnt+=1
            if cnt==n-1:
                return temp
        return 0