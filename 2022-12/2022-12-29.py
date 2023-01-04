from collections import defaultdict
from typing import List
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        m=defaultdict(int)
        for num in nums1: m[num]|=1
        for num in nums2: m[num]|=2
        for num in nums3:  m[num]|=4
        res=[]
        for k in m:
            if m[k]==1 or m[k]==2 or m[k]==4:
                continue
            res.append(k)
        return res
    
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        def check(d):
            cnt,x0=1,price[0]
            for x in price:
                if x>=x0+d:
                    cnt+=1
                    x0=x
            return cnt>=k
        left,right=0,price[-1]-price[0]+1
        while left+1<right:
            # print(left,right)
            mid=(left+right)//2
            if check(mid):
                left=mid
            else:
                right=mid
        return left