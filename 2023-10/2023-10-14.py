from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in range(0,len(nums)):
            res^=nums[i]
        return res
    
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res,cnt=0,0
        m=dict()
        for i in range(len(nums)-1,-1,-1):
            if m.get(nums[i]) is None and nums[i]<=k:
                cnt+=1
                m[nums[i]]=1
            res+=1
            if cnt>=k:
                break
        return res
    
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        m=defaultdict(int)
        for num in nums:
            m[num]+=1
        res=0
        for k in m:
            if m[k]<2:
                return -1
            res+=(m[k]+2)//3
        return res


class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        sum = 0xfffff
        res = 0
        for num in nums:
            sum&=num
            if sum==0:
                res+=1
                sum=0xfffff
        return max(res,1)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=[0 for _ in range(0,32)]
        def binaryNum(num,res):
            if num<0:
                res[31]+=1
                num+=0x80000000
            for i in range(30,-1,-1):
                if num>=1<<i:
                    num-=1<<i
                    res[i]+=1
        for num in nums:
            binaryNum(num,res)
        ans=0
        for i in range(30,-1,-1):
            if res[i]%3!=0:
                ans+=1<<i
        if res[31]%3!=0:
            ans-=0x80000000
        return ans
    
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    res=max(res,(nums[i]-nums[j])*nums[k])
        return res
    
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        pre=[0 for _ in range(0,n)]
        suf=[0 for _ in range(0,n)]
        pre[0],suf[n-1]=0,0
        for i in range(1,n):
            pre[i]=max(pre[i-1],nums[i-1])
        for i in range(n-2,-1,-1):
            suf[i]=max(suf[i+1],nums[i+1])
        res=0
        for i in range(0,n):
            res=max(res,(pre[i]-nums[i])*suf[i])
        return res
                