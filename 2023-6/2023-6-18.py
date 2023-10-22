from functools import cache
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        flag=[[0 for _ in range(0,n)] for _ in range(0,m)]
        res=0
        def check(i,j):
            res=True
            q=[[i,j]]
            tos=[[-1,0],[0,-1],[1,0],[0,1]]
            flag[i][j]=1
            while len(q)>0:
                temp=q
                q=[]
                for v in temp:
                    if v[0]==m-1 or v[0]==0 or v[1]==n-1 or v[1]==0:
                        res=False
                    for to in tos:
                        x,y=v[0]+to[0],v[1]+to[1]
                        if x<m and x>=0 and y<n and y>=0 and grid[x][y]==0 and flag[x][y]==0:
                            flag[x][y]=1
                            q.append([x,y]) 
            return res
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j]==0 and flag[i][j]==0 and check(i,j):
                    res+=1
        return res
    
    
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        res=0
        while mainTank>=5 and additionalTank>0:
            res+=50
            additionalTank-=1
            mainTank-=4
        res+=mainTank*10
        return res
    
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        res=1e9+7
        nums.sort()
        for i in range(1,len(nums)):
            res=min(res,nums[i]-nums[i-1])
        return res
    
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n=1<<len(nums)
        mod=1e9+7
        @cache
        def dfs(i,j):
            if i==0:
                return 1
            res=0
            for k in range(0,len(nums)):
                if i>>k&1>0 and (nums[j]%nums[k]==0 or nums[k]%nums[j]==0):
                    res=(res+dfs(i^(1<<k),k))%mod
            return res
        res=0
        for k in range(0,len(nums)):
            res=(res+dfs((n-1)^(1<<k),k))%mod
        return int(res)
        
