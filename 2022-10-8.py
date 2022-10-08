
from typing import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        noZero=sorted(Counter(word).values())
        if len(noZero)==1: return True
        return (noZero[0]==1 and noZero[1]==noZero[-1]) or (
            noZero[0]==noZero[-2] and noZero[-1]-1==noZero[0]
        )
        
        
class LUPrefix:
    def __init__(self, n: int):
        self.m=dict()
        self.cur=0

    def upload(self, video: int) -> None:
        self.m[video]=1
        temp=self.cur+1
        while(self.m.get(temp) is not None): temp+=1
        self.cur=temp-1

    def longest(self) -> int:
        return self.cur
    
    
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans=0
        if len(nums1)%2==1:
            for i in range(0,len*nums2): ans^=nums2[i]
        if len(nums2)%2==1:
            for i in range(0,len(nums1)): ans^=nums1[i]
        return ans