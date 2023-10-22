from collections import defaultdict


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        def dfs(i):
            if 2*i>=n:
                return 0,cost[i-1]
            ops1,sum1=dfs(2*i)
            ops2,sum2=dfs(2*i+1)
            return ops1+ops2+abs(sum1-sum2),max(sum1,sum2)+cost[i-1]
        res,_=dfs(1)
        return res
    
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        res=[0 for _ in range(0,len(queries))]
        t=[0 for _ in range(0,n)]
        t[queries[0][0]]=queries[0][1]
        for i in range(1,len(queries)):
            idx,v=queries[i][0],queries[i][1]
            res[i]=res[i-1]
            if idx>0:
                if t[idx]!=0 and t[idx]==t[idx-1]:
                    res[i]-=1
                if t[idx-1]==v:
                    res[i]+=1
            if idx<n-1:
                if t[idx]!=0 and t[idx]==t[idx+1]:
                    res[i]-=1
                if t[idx+1]==v:
                    res[i]+=1
            t[idx]=v
        return res
    
class FrequencyTracker:
    
    def __init__(self):
        self.m,self.cnt=defaultdict(int),defaultdict(int)

    def add(self, number: int) -> None:
        self.m[number]+=1
        self.cnt[self.m[number]]+=1
        self.cnt[self.m[number]-1]-=1

    def deleteOne(self, number: int) -> None:
        if self.m[number]<=0: return
        self.m[number]-=1
        self.cnt[self.m[number]]+=1
        self.cnt[self.m[number]+1]-=1

    def hasFrequency(self, frequency: int) -> bool:
        return self.cnt[frequency]>0
    
    
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        m=defaultdict(int)
        for v in nums:
            m[v]+=1
        m2=defaultdict(int)
        res=[0 for _ in range(0,len(nums))]
        for (i,v) in enumerate(nums):
            m2[v]+=1
            m[v]-=1
            if m[v]==0:
                m.pop(v)
            res[i]=len(m2)-len(m)
        return res
    
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def cnt(player):
            s=0
            for (i,v) in enumerate(player):
                if (i>0 and player[i-1]==10) or (i>1 and player[i-2]==10):
                    s+=2*v
                else:
                    s+=v
            return s
        if cnt(player1)>cnt(player2):return 1
        if cnt(player1)==cnt(player2): return 0
        return 2