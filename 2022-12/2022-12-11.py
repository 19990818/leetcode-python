from cmath import inf
from collections import defaultdict
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res=0
        cur=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<cur+1:
                cur+=1
                res+=cur-nums[i]
            else:
                cur=nums[i]
        return res
    
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res=0
        for v in strs:
            if v.isdigit():
                res=max(res,int(v))
            else:
                res=max(res,len(v))
        return res
    
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        res=-inf
        n=len(vals)
        g=[[]for _ in range(0,n)]
        for v in edges:
            g[v[0]].append(vals[v[1]])
            g[v[1]].append(vals[v[0]])
        for i in range(0,n):
            g[i]=sorted(g[i],reverse=True)
        for i in range(0,n):
            temp=vals[i]
            res=max(res,temp)
            j=0
            while j<k and j<len(g[i]):
                temp+=g[i][j]
                res=max(res,temp)
                j+=1
        return res
    
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        def getMaxDistance(i):
            start,end=stones[0],stones[-1]
            res=0
            while(i<len(stones)):
                res=max(res,stones[i]-start)
                start=stones[i]
                i+=2
            return res
        return max(getMaxDistance(1),getMaxDistance(2))
    
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res=0
        for i in range(0,len(grid)):
            grid[i].sort()
        for j in range(0,len(grid[0])):
            temp=0
            for i in range(0,len(grid)):
                temp=max(temp,grid[i][j])
            res+=temp
        return res
    
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        res=-1
        m=defaultdict(int)
        travel=defaultdict(int)
        for v in nums:
            m[v]=1
        for v in nums:
            if travel[v]==0:
                cur,cnt=v,1
                while m[cur*cur]==1:
                    cnt+=1
                    cur=cur*cur
                    travel[cur]=1
                if cnt>=2 and cnt>res:
                    res=cnt
        return res
        