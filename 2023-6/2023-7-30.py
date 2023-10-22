
from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow,fast=head.next,head.next.next
        while slow is not None and fast is not None and fast.next is not None and slow !=fast:
            slow,fast=slow.next,fast.next.next
        if slow == fast:
            slow =head
            while slow!=fast:
                slow,fast=slow.next,fast.next    
            return slow
        return None
    
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res=0
        for hour in hours:
            if hour>=target:
                res+=1
        return res



class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res=0
        m,temp=defaultdict(int),defaultdict(int)
        for num in nums:
            m[num]=1
        left,right=0,0
        while left<=right:
            while right<len(nums) and len(temp)<len(m):
                temp[nums[right]]+=1
                right+=1
            if len(temp)==len(m):
                res+=len(nums)-right+1
            if left<len(nums):
                temp[nums[left]]-=1
                if temp[nums[left]]==0:
                    temp.pop(nums[left])
            left+=1
        return res
    
class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        m=defaultdict(int)
        ss=[a,b,c]
        res=a+b+c
        def dfs(cur):
            
            nonlocal res
            if len(m)==len(ss):
                if len(cur)<len(res) or (len(cur)==len(res) and cur<res):
                    res=cur
                return
            for i,s in enumerate(ss):
                if m[i]==0:
                    if cur.find(s)!=-1:
                        
                        m[i]=1
                        dfs(cur)
                        m.pop(i)
                        continue
                    for j in range(0,len(cur)+1):
                        if len(cur)-j<=len(s) and cur[j:]==s[0:len(cur)-j]:
                            m[i]=1
                            dfs(cur+s[len(cur)-j:])
                            m.pop(i)
                            break
        dfs("")
        return res