from collections import defaultdict


class Solution:
    def isValid(self, s: str) -> bool:
        pre=s
        while pre!=pre.replace("abc",""):
            pre=pre.replace("abc","")
        return pre==""
    
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums)*k+k*(k-1)/2

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ma,mb=defaultdict(int),defaultdict(int)
        res=[0 for _ in range(0,len(A))]
        def cnt(ma,mb):
            res=0
            for k in ma:
                if mb[k]==1:
                    res+=1
            return res
        for i in range (0,len(A)):
            ma[A[i]]=1
            mb[B[i]]=1
            res[i]=cnt(ma,mb)
        return res
    
    
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        res=0
        travel=defaultdict(int)
        def check(x,y):
            return x<m and x>=0 and y>=0 and y<n and grid[x][y]>0 and travel[x*n+y]==0
        def bfs(i,j):
            res=0
            tos=[[-1,0],[0,-1],[1,0],[0,1]]
            q=[[i,j]]
            while len(q)>0:
                temp=q
                q=[]
                for i in range(0,len(temp)):
                    res+=grid[temp[i][0]][temp[i][1]]
                    for to in tos:
                        curx,cury=temp[i][0]+to[0],temp[i][1]+to[1]
                        if check(curx,cury):
                            travel[curx*n+cury]=1
                            q.append([curx,cury])
            return res
        for (i,g) in enumerate(grid):
            for (j,v) in enumerate(grid[i]):
                if v>0 and travel[i*n+j]==0:
                    travel[i*n+j]=1
                    res=max(res,bfs(i,j))
        return res