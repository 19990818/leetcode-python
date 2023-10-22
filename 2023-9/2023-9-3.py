

from ast import List
from collections import defaultdict


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n=len(dist)
        t=[0 for _ in range(0,n)]
        for i in range(0,n):
            t[i]=(dist[i]-1)//speed[i]+1
        t.sort()
        for i in range(0,n):
            if t[i]<i+1:
                return i
        return n
    
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        for i in range(0,len(s1)):
            flag=1
            if i>1:
                flag=-1
            if s1[i]==s2[i] or (s1[i]==s2[i+2*flag] and s1[i+2*flag]==s2[i]):
                continue
            return False
        return True
    
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        os1,os2,es1,es2=[],[],[],[]
        for i in range(0,len(s1)):
            if i%2==0:
                os1.append(s1[i])
                os2.append(s2[i])
            else:
                es1.append(s1[i])
                es2.append(s2[i])
        os1.sort()
        os2.sort()
        es1.sort()
        es2.sort()
        return "".join(os1)=="".join(os2) and "".join(es1)=="".join(es2)
    
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        res,sum=0,0
        ma=defaultdict(int)
        for i in range(0,k):
            ma[nums[i]]+=1
            sum+=nums[i]
        if len(ma)>=m:
            res=sum
        for i in range(k,len(nums)):
            sum=sum-nums[i-k]+nums[i]
            ma[nums[i-k]]-=1
            if ma[nums[i-k]]==0:
                ma.pop(nums[i-k])
            ma[nums[i]]+=1
            if len(ma)>=m:
                res=max(res,sum)
        return res
    
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cnt = [0 for _ in range(0,numCourses)]
        out=[[] for _ in range(0,numCourses)]
        for v in prerequisites:
            cnt[v[0]]+=1
            out[v[1]].append(v[0])
        res=[]
        while len(res)<numCourses:
            flag=False
            for i in range(0,numCourses):
                if cnt[i]==0:
                    cnt[i]-=1
                    flag=True
                    res.append(i)
                    for v in out[i]:
                        cnt[v]-=1
            if not flag:
                return []
        return res
        
                