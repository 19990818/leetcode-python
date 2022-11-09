from cmath import inf


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid=[[inf for _ in range(0,n)] for _ in range(0,n)]
        for mine in mines:
            grid[mine[0]][mine[1]]=0
        for i in range(0,n):
            left,right,up,down=0,0,0,0
            for j in range(0,n):
                if grid[i][j]==0: left=0
                else: left+=1
                if grid[j][i]==0: up=0
                else: up+=1
                grid[i][j]=min(grid[i][j],left)
                grid[j][i]=min(grid[j][i],up)
            left,right,up,down=0,0,0,0
            for k in range(n-1,-1,-1):
                if grid[i][k]==0: right=0
                else:right+=1
                if grid[k][i]==0: down=0
                else:down+=1
                grid[i][k]=min(grid[i][k],right)
                grid[k][i]=min(grid[k][i],down)
        res=0
        for i in range(0,n):
            for j in range(0,n):
                res=max(res,grid[i][j])
        return res