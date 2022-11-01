

from math import sqrt


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        n=len(nums)+2
        psum,sum=n*(n+1)*(2*n+1)/6,n*(n+1)/2
        for num in nums:
            psum-=num*num
            sum-=num
        return [int((sum+sqrt(2*psum-sum*sum))/2),int((sum-sqrt(2*psum-sum*sum))/2)]