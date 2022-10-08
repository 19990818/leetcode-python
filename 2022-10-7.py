

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans,temp=0,nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                temp+=nums[i]
            else:
                ans=max(ans,temp)
                temp=nums[i]
        ans=max(ans,temp)
        return ans
            


