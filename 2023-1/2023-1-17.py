from collections import defaultdict
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        m=defaultdict(int)
        def rev(a):
            res=0
            while a>0:
                res=res*10+a%10
                a//=10
            return res
        for num in nums:
            m[num-rev(num)]+=1
        res=0
        mod=1e9+7
        for v in m:
            res=(res+m[v]*(m[v]-1)//2)%mod
        return int(res)
            