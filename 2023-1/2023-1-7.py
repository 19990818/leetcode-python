from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        preSum,m=0,dict()
        m[preSum]=0
        for (i,v) in enumerate(nums):
            preSum=preSum+v
            m[preSum]=i+1
        res=-1
        if preSum<x: return res
        preSum=0
        for i in range(0,len(nums)):
            if m.get(x-preSum) is not None:
                if res==-1:
                    res=i+m[x-preSum]
                else:
                    res=min(res,i+m[x-preSum])
            preSum=preSum+nums[len(nums)-1-i]
        return res