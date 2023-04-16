from heapq import heappop, heappush
from math import gcd
import queue


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        temp="aeiouAEIOU"
        part,sum=0,0
        for i in range(0,len(s)):
            if temp.find(s[i])!=-1:
                sum+=1
                if i<len(s)/2:
                    part+=1
        return sum==2*part
    
    
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int: 
        res=0
        q=[]
        m=dict()
        for i in range(0,len(apples)):
            if m.get(i+days[i]) is None or m[i+days[i]]==0:
                heappush(q,i+days[i])
                m[i+days[i]]=0
            # print("queue",q)
            m[i+days[i]]+=apples[i]
            res=self.eat(res,i,m,q)
        i=len(apples)
        while len(q)>0:
            res=self.eat(res,i,m,q)
            i+=1
        return res
    def eat(self,res,i,m,q):
        temp=heappop(q)
        while temp<=i and len(q)>0:
            temp=heappop(q)
        m[temp]-=1
        if m[temp]>=0 and temp>i:
            res+=1
            if m[temp]>0: heappush(q,temp)
        return res

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        for i in range(n-1):
            for j in range(l+1,n):
                if gcd(nums[i],nums[j])!=1:
                    l=j
            if l==i:return l
        return -1