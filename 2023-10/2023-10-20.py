
from ast import List
from collections import defaultdict


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        def isBulky(length,width,height):
            return length>=1e4 or width>=1e4 or height>=1e4 or length*width*height>=1e9
        bulky=isBulky(length,width,height)
        if mass>=100 and bulky:
            return "Both"
        if mass>=100 and not bulky:
            return "Heavy"
        if bulky:
            return "Bulky"
        return "Neither"
    
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent=[i for i in range(0,n)]
        def find(c):
            if parent[c]==c:
                return c
            parent[c]=find(parent[c])
            return parent[c]
        def merge(a,b):
            a=find(a)
            b=find(b)
            if a==b:
                return
            parent[a]=b
        for edge in edges:
            merge(edge[0],edge[1])
        m=defaultdict(int)
        for i in range(0,n):
            m[find(i)]+=1
        res=0
        for k in m:
            res+=(n-m[k])*m[k]
        return res//2     
    
    
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        ss = sum(nums)
        c,part = target//ss, target%ss
        m=defaultdict(int)
        flag=False
        minCnt=len(nums)
        if part==0:
            return c*len(nums)
        m[0]=-1
        prefix=0
        for i in range(0,2*len(nums)):
            prefix+=nums[i%len(nums)]
            m[prefix]=i
            if m[prefix-part]!=0:
                minCnt=min(minCnt,i-m[prefix-part])
                flag=True
        if flag:
            return c*len(nums)+minCnt
        return -1


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        cntm=n//m
        end=cntm*m
        return n*(n+1)//2-(end+m)*cntm
    
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        diff=[]
        for i in range(0,len(s1)):
            if s1[i]!=s2[i]:
                diff.append(i)
        if len(diff)%2!=0:
            return -1
        part=len(diff)//2
        dp=[0 for _ in range(0,part+1)]
        def cnt1(start,end):
            res=0
            for i in range(2*start,2*end,2):
                res+=min(diff[i+1]-diff[i],x)
            return res
        def cnt2(start,end):
            res=0
            for i in range(2*start+1,2*end-1,2):
                res+=min(diff[i+1]-diff[i],x)
            res+=min(diff[2*end-1]-diff[start],x)
            return res
        for i in range(1,part+1):
            dp[i]=1e5
            for j in range(0,i):
                dp[i]=min(dp[i],dp[j]+min(cnt1(j,i),cnt2(j,i)))
        return dp[part]
                                            