class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        dp=[[0 for _ in range(0,k+1)] for _ in range(0,len(nums))]
        sum=[0 for _ in range(0,len(nums)+1)]
        for i in range(0,len(nums)):
            sum[i+1]=sum[i]+nums[i]
            dp[i][1]=sum[i+1]/(i+1)
        for i in range(0,len(nums)):
            c=2
            while c<=k and c<=i+1:
                for j in range(0,i):
                    dp[i][c]=max(dp[i][c],dp[j][c-1]+(sum[i+1]-sum[j+1])/(i-j))
                c+=1
        return dp[len(nums)-1][k]