from ast import List
from collections import defaultdict


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        res=0
        sum=0
        intervals=defaultdict(int)
        intervals[0]=1
        for i in range(0,len(nums)):
            if nums[i]%modulo==k:
                sum+=1
            mod=sum%modulo
            res+=intervals.get((mod-k+modulo)%modulo,0)
            intervals[(mod%modulo)]+=1
        return res
    
    
class Solution:
    def minimumOperations(self, num: str) -> int:
        flag0,flag5=False,False
        for i in range(len(num)-1,-1,-1):
            if int(num[i])==5:
                if flag0:
                    return len(num)-i-2
                flag5=True
            if int(num[i])==0:
                if flag0:
                    return len(num)-i-2
                flag0=True
            if (int(num[i])==2 or int(num[i])==7) and flag5:
                return len(num)-i-2
        if flag0:
            return len(num)-1
        return len(num)    
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.robHelp(nums[0:len(nums)-1]),self.robHelp(nums[1:]))
        
    def robHelp(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        n=len(nums)
        dp=[[0 for _ in range(0,2)] for _ in range(0,n)]
        dp[0][0],dp[0][1]=0,nums[0]
        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1])
            dp[i][1]=max(dp[i][1],dp[i-1][0]+nums[i])
            if i>1:
                dp[i][1]=max(dp[i][1],dp[i-2][1]+nums[i])
        return max(dp[n-1][0],dp[n-1][1])
    
    
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones=0
        for c in s:
            if c=="1":
                ones+=1
        res=""
        for i in range(0,ones-1):
            res+="1"
        for i in range(ones-1,len(s)-1):
            res+="0"
        res+="1"
        return res
    
    
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        res=0
        for i in range(0,len(maxHeights)):
            temp=0
            cur=maxHeights[i]
            for j in range(i,-1,-1):
                cur=min(cur,maxHeights[j])
                temp+=cur
            cur=maxHeights[i]
            for j in range(i+1,len(maxHeights)):
                cur=min(cur,maxHeights[j])
                temp+=cur
            res=max(temp,res)
        return res
    
        