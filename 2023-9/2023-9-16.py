from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[0 for _ in range(0,2)] for _ in range(0,n)]
        dp[0][0],dp[0][1]=0,nums[0]
        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1])
            dp[i][1]=max(dp[i][1],dp[i-1][0]+nums[i])
            if i>1:
                dp[i][1]=max(dp[i][1],dp[i-2][1]+nums[i])
        return max(dp[n-1][0],dp[n-1][1])
    
    
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res=0
        print(int("123"))
        for i in range(low,high+1):
            s=str(i)
            temp=0
            if len(s)%2==0:
                for j in range(0,len(s)):
                    flag=1
                    if j>=len(s)/2:
                        flag=-1
                    temp+=flag*int(s[j])
                if temp==0:
                    res+=1
        return res