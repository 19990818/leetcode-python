class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp=[[0 for _ in range(0,query_row+1)] for _ in range(0,query_row+1)]
        dp[0][0]=poured
        for i in range(1,query_row+1):
            for j in range(0,i+1):
                if j==0:
                    dp[i][j]=max((dp[i-1][j]-1)/2,0)
                elif j==i:
                    dp[i][j]=max((dp[i-1][j-1]-1)/2,0)
                else:
                    dp[i][j]=max((dp[i-1][j-1]-1)/2,0)+max((dp[i-1][j]-1)/2,0)
        print(dp)
        return min(dp[query_row][query_glass],1)