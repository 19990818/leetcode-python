from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left,right=1,max(nums)
        while left<right:
            mid=(right+left)//2
            cnt=0
            for num in nums:
                cnt+=num//mid
                if num%mid==0: cnt-=1
            if cnt<=maxOperations:
                right=mid
            else:
                left=mid+1
        return left