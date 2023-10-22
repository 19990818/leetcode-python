# Definition for singly-linked list.
from ast import List
from collections import Counter
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode(0)
        cur=res
        c=0
        while l1 is not None or l2 is not None:
            sum=c
            if l1 is not None:
                sum+=l1.val
                l1=l1.next
            if l2 is not None:
                sum+=l2.val
                l2=l2.next
            c=sum//10
            cur.next=ListNode(sum%10)
            cur=cur.next
        if c>0:
            cur.next=ListNode(c)
        return res.next
    
    
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(a,b):
            while b>0:
                a,b=b,a%b
            return a
        res=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                a,b=ord(str(nums[i])[0])-ord('0'),nums[j]%10
        if gcd(a,b)==1: 
                    res+=1
        return res 
    
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        i=1
        while num1>0:
            num1-=num2
            if bin(num1).count("1")<=i and num1>=i:
                return i
            i+=1
        return -1
    
    
class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        res,cnt=1,0
        mod=1e9+7
        flag=False
        for num in nums:
            if num==1:
                if flag:
                    res=(res*cnt)%mod
                    cnt=1
                    flag=True
            else:
                cnt+=1
        if flag:
            return int(res)
        return 0
   
   
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        res,flag,cnt=0,False,0
        start=0
        for i in range(0,len(nums)):
            if nums[i]%2==0 and nums[i]<=threshold:
                if (i-start)%2==0:
                    cnt+=1
                else:
                    cnt=1
                    start=i
                flag=True
            elif flag and nums[i]<=threshold and (i-start)%2==1:
                cnt+=1
            else:
                cnt=0
                flag=False
            res=max(res,cnt)
        return res