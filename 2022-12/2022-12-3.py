
from collections import defaultdict
from typing import List


class Solution:
    def secondHighest(self, s: str) -> int:
        m=defaultdict(int)
        for c in s:
            if c.isdigit():m[int(c)]=1
        temp=0
        for i in range(9,-1,-1):
            if m[i]==1:
                temp+=1
                if temp==2:
                    return i
        return -1
    
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        x,y=tomatoSlices//2-cheeseSlices,2*cheeseSlices-tomatoSlices//2
        if tomatoSlices%2==0 and x>=0 and y>=0:
            return [x,y]
        return []
    
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res=[]
        for i in range(len(str(low)),len(str(high))+1):
            s,d=self.getStaAndDis(i)
            for j in range(0,10-i):
                if s<=high and s>=low:
                    res.append(s)
                s+=d
        return res
    def getStaAndDis(self,l:int):
        s,d=0,0
        for i in range(1,l+1):
            s=s*10+i
            d=d*10+1
        return s,d
    
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        m=defaultdict(int)
        sorted(nums)
        for num in nums:
            m[num]+=1
        for num in nums:
            if m[num]!=0:
                for i in range(0,k):
                    if m[num+i]==0:return False
                    m[num+i]-=1
        return True
    