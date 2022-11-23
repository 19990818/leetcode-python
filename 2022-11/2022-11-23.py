from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        m=defaultdict(int)
        res=0
        for i in range(lowLimit,highLimit+1):
            m[self.numSum(i)]+=1 
        for v in m:
            res=max(res,m[v])
        return res
    def numSum(self,n)->int:
        res=0
        while n>0:
            res+=n%10
            n=n//10
        return res
    
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        res=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                res=max(res,self.dfs(grid,i,j))
        return res
        
    def dfs(self,grid,i,j)->int:
        if i>=len(grid) or i<0 or j>=len(grid[0]) or j<0 or grid[i][j]==0:
            return 0
        cur=grid[i][j]
        grid[i][j]=0
        res=0
        res=max(res,cur+self.dfs(grid,i-1,j))
        res=max(cur+self.dfs(grid,i,j+1),res)
        res=max(cur+self.dfs(grid,i+1,j),res)
        res=max(cur+self.dfs(grid,i,j-1),res)
        grid[i][j]=cur
        return res