

from ast import List
from typing import Optional


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,m+n):
            nums1[i]=nums2[i-m]
        nums1.sort()
        
        
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def splitNum(a:int):
            res=[]
            while a>0:
                res.append(a%10)
                a//=10
            return res
        def isMaxNumSame(a:int,b:int):
            ans=splitNum(a)
            ans.sort()
            bns=splitNum(b)
            bns.sort()
            return ans[-1]==bns[-1]
        res=-1
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if isMaxNumSame(nums[i],nums[j]):
                    res=max(res,nums[i]+nums[j])
        return res
            
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next          
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums=[]
        while head is not None:
            nums.append(head.val)
            head=head.next
        res=None
        c=0
        for i in range(len(nums)-1,-1,-1):
            t=ListNode((c+nums[i]*2)%10)
            c=(c+nums[i]*2)//10
            t.next=res
            res=t
        if c>0:
            t=ListNode(c)
            t.next=res
            res=t
        return res