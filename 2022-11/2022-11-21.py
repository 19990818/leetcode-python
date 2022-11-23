class Solution:
    def soupServings(self, n: int) -> float:
        if n>5000:return 1
        if n%25==0:n=n//25
        else: n=n//25+1
        dp=[[0 for _ in range(0,n+1)]for _ in range(0,n+1)]
        dp[0][0]=0.5
        for i in range(1,n+1):
            dp[0][i],dp[i][0]=1,0
        for i in range(1,n+1):
            for j in range(1,n+1):
                dp[i][j]=(dp[max(i-4,0)][j]+dp[max(i-3,0)][max(j-1,0)]
                          +dp[max(i-2,0)][max(j-2,0)]+dp[max(i-1,0)][max(j-3,0)])/4
        return dp[n][n]