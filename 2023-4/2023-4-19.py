
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp=[0 for _ in range(0,len(arr)+1)]
        dp[len(arr)]=0
        dp[len(arr)-1]=arr[-1]
        for i in range(len(arr)-2,-1,-1):
            j=i
            ma=arr[i]
            while j<len(arr) and j<i+k:
                ma=max(ma,arr[j])
                dp[i]=max(dp[i],ma*(j-i+1)+dp[j+1])
                j+=1
        return dp[0]
    
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        res=[0 for _ in range(0,len(grid[0]))]
        for j in range(0,len(grid[0])):
            for i in range(0,len(grid)):
                cur=str(grid[i][j])
                res[j]=max(res[j],len(cur))
        return res
    
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ma=0
        for i in range(0,len(nums)):
            ma=max(ma,nums[i])
            nums[i]+=ma
        res=[0 for _ in range(0,len(nums))]
        res[0]=nums[0]
        for i in range(1,len(nums)):
            res[i]=res[i-1]+nums[i]
        return res