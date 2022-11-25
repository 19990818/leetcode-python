

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        dp=[0 for _ in range(0,len(nums)+1)]
        dp2=[0 for _ in range(0,len(nums)+1)]
        for i in range(0,len(nums)):
            if nums[i]<=right and nums[i]>=left:
                dp[i+1]=dp2[i]+1
            elif nums[i]<left:
                dp[i+1]=dp[i]
                dp2[i+1]=dp2[i]+1
        res=0
        for v in dp:
            res+=v
        return res
        