

from math import inf
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans=0
        for word in words:
            if len(word)>=len(pref) and word[0:len(pref)]==pref:
                ans+=1
        return ans
    
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        def isBulky(length,width,height):
            return length*width*height>=10**9 or length>=10**4 or width>=10**4 or height>=10**4
        def isHeavy(mass):
            return mass>=100
        if isBulky(length,width,height) and isHeavy(mass):
            return "Both"
        if isBulky(length,width,height):
            return "Bulky"
        if isHeavy(mass):
            return "Heavy"
        return "Neither"


class DataStream:
    cnt,k,v=0,0,0
    def __init__(self, value: int, k: int):
        self.k=k
        self.v=value

    def consec(self, num: int) -> bool:
        if num==self.v:
            self.cnt+=1
        else:
            self.cnt=0
        return self.cnt>=self.k
    
    
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        ans=0
        for num in nums:
            ans^=num
        return ans
    
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        mn=inf
        n=len(stations)
        sum=[0 for _ in range(0,n+1)]
        
        for i in range(0,n):
            sum[i+1]=sum[i]+stations[i]
        for i in range(0,n):
            stations[i]=sum[min(n,i+r+1)]-sum[max(0,i-r)]
            mn=min(mn,stations[i])
        def check(mid):
            need,sum_d=0,0
            diff=[0 for _ in range(n)]
            for (i,v) in enumerate(stations):
                sum_d+=diff[i]
                m=mid-v-sum_d
                if m>0:
                    need+=m
                    if need>k: return False
                    sum_d+=m
                    if i+2*r+1<n: diff[i+2*r+1]-=m
            return True
        left,right=mn,mn+k+1
        while left+1<right:
            mid=(left+right)//2
            if check(mid):
                left=mid
            else: right=mid
        return left