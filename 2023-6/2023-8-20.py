from ast import List
from collections import defaultdict


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]<target:
                    res+=1
        return res
    
    
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i,j=0,0
        while i<len(str1) and j<len(str2):
            t=ord(str2[j])-ord(str1[i])
            if t==0 or t==1 or (str2[j]=='a' and str1[i]=='z'):
                j+=1
            i+=1
        return j>=len(str2)
    

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnts=[[0 for _ in range(0,3)] for _ in range(0,len(nums)+1)]
        for i in range(0,len(nums)):
            for j in range(0,3):
                cnts[i+1][j]=cnts[i][j]
            cnts[i+1][nums[i]-1]+=1
        print(cnts)
        res=len(nums)
        for i in range(0,len(nums)+1):
            for j in range(i,len(nums)+1):
                cnt1=i-cnts[i][0]
                cnt2=j-i-cnts[j][1]+cnts[i][1]
                cnt3=len(nums)-j-cnts[len(nums)][2]+cnts[j][2]
                res=min(res,cnt1+cnt2+cnt3)
        return res
    
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        res=""
        for word in words:
            res+=word[0]
        return res==s
    
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        cnt=0
        m=defaultdict(int)
        i=1
        res=0
        while cnt<n:
            if i<k and m[k-i]==1:
                i+=1
                continue
            m[i]=1
            res+=i
            i,cnt=i+1,cnt+1
        return res


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        dp=[0 for _ in range(0,n+1)]
        k=0
        offers=sorted(offers,key=lambda x:x[1])
        for i in range(0,n):
            dp[i+1]=dp[i]
            while k<len(offers) and i==offers[k][1]:
                dp[i+1]=max(dp[i+1],dp[offers[k][0]]+offers[k][2])
                k+=1
        return dp[n]