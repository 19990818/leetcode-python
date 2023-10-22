

from ast import List
from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode(0)
        res.next=head
        cur=res
        while head is not None and head.next is not None:
            temp=head.next
            next=head.next.next
            cur.next=temp
            temp.next=head
            head.next=next
            cur=head
            head=next
        return res.next
    
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100-(purchaseAmount+5)//10*10
    
    
class Solution:
    def gcd(self,a,b):
        while b!=0:
            a,b=b,a%b
        return a
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode(0)
        res.next=head
        while head.next is not None:
            temp=head.next
            insertNode=ListNode(self.gcd(head.val,head.next.val))
            head.next=insertNode
            insertNode.next=temp
            head=temp
        return res.next
    
    
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        m=dict()
        n=len(nums)
        for i in range(0,n):
            if m.get(nums[i]) is None:
                m[nums[i]]=[i]
            else:
                m[nums[i]].append(i)
        res=n
        for k in m:
            temp=0
            for i in range(0,len(m[k])):
                if i<len(m[k])-1:
                    temp=max(temp,(m[k][i+1]-m[k][i])//2)
                else:
                    temp=max(temp,(n-m[k][i]+m[k][0])//2)
            res=min(res,temp)
        return res
    
class Solution:
    def finalString(self, s: str) -> str:
        res=""
        def reverseStr(s):
            ans=""
            for c in s:
                ans=c+ans
            return ans
        for ss in s:
            if ss=="i":   
                res=reverseStr(res)
            else:
                res+=ss
        return res
        