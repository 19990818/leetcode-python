class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n=len(nums)
        sum=[[0 for _ in range(0,n)] for _ in range(0,n)]
        for i in range(0,n):
            sum[i][i]=nums[i]
            for j in range(i+1,n):
                sum[i][j]=sum[i][j-1]+nums[j]
        res=0
        for i in range(0,n-firstLen+1):
            for j in range(0,i-secondLen+1):
                res=max(res,sum[i][i+firstLen-1]+sum[j][j+secondLen-1])
            for j in range(i+firstLen,n-secondLen+1):
                res=max(res,sum[i][i+firstLen-1]+sum[j][j+secondLen-1])
        return res