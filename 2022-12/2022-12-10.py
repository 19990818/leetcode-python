

from collections import defaultdict
from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for i in range(0,len(cuboids)):
            cuboids[i].sort(reverse=True)
        cuboids.sort(reverse=True)
        dp=[0 for _ in range(0,len(cuboids))]
        res=0
        for i in range(0,len(cuboids)):
            dp[i]=cuboids[i][0]
            for j in range(0,i):
                if cuboids[i][2]<=cuboids[j][2] and cuboids[i][1]<=cuboids[j][1]:
                    dp[i]=max(dp[i],dp[j]+cuboids[i][0])
            res=max(res,dp[i])
        return res
    
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors=[0 for _ in range(0,len(arr)+1)]
        for (i,v) in enumerate(arr):
            xors[i+1]=xors[i]^v
        res=[0 for _ in range(0,len(queries))]
        for (i,v) in enumerate(queries):
            res[i]=xors[v[0]]^xors[v[1]+1]
        return res
    
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q=[start]
        m=defaultdict(int)
        n=len(arr)
        def canNext(cur,offset):
            return cur+offset<n and cur+offset>=0 and m[cur+offset]==0
        while len(q)>0:
            temp=q
            q=[]
            while len(temp)>0:
                cur=temp[1]
                temp=temp[1:]
                if arr[cur]==0:
                    return True
                if canNext(cur,arr[cur]):
                    m[cur+arr[cur]]=1
                    q.append(cur+arr[cur])
                if canNext(cur,-arr[cur]):
                    m[cur-arr[cur]]=1
                    q.append(cur-arr[cur])
        return False
        