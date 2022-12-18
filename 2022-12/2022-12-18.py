from cmath import inf
from collections import defaultdict
from typing import List


class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        preSum,g=[0],[]
        for (i,v) in enumerate(nums):
            if v==1:
                g.append(i-len(g))
                preSum.append(preSum[-1]+g[-1])
        res=inf
        m=len(g)
        for i in range(0,m-k+1):
            mid=i+k//2
            r=g[mid]
            f=r*(1-k%2)+preSum[k+i]-preSum[mid+1]+preSum[i]-preSum[mid]
            res=min(res,f)
        return res
    
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        m=len(words)
        res=0
        def isSimlar(a,b):
            m1,m2=defaultdict(int),defaultdict(int)
            for c in a:
                m1[c]=1
            for c in b:m2[c]=1
            return m1==m2
        for i in range(0,m):
            for j in range(i+1,m):
                if isSimlar(words[i],words[j]):
                    res+=1
        return res
    
class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            s,t=n,0
            i=2
            while i*i<=s:
                while n%i==0:
                    t+=i
                    n//=i
                i+=1
            if n>1: t+=n
            if t==s:return t
            n=t
                    
                
        