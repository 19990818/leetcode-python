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
        # 当我们进行选择的时候 因为left不发生改变的话 会导致mid也不变化
        # 造成死循环的情况 这种情况在left+1=right的时候发生 因此直接干掉这种情况
        # 在这种情况中right实际上永远取不到 因此区间为[left,right)
        
        while left+1<right:
            # print(left,right)
            mid=(left+right)//2
            if check(mid):
                left=mid
            else:
                right=mid
        return left