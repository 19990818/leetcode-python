from math import inf
from typing import List


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr=sentence.split(" ")
        for i in range(0,len(arr)):
            if arr[(i+1)%len(arr)][0]!=arr[i][-1]:
                return False
        return True
    
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i,j=0,len(skill)-1
        temp=skill[i]+skill[j]
        ans=0
        while i<j:
            if temp!=skill[i]+skill[j]:
                return -1
            ans+=skill[i]*skill[j]
            i,j=i+1,j-1
        return ans
    
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g=[[] for _ in range(0,n+1)]
        for v in roads:
            g[v[0]].append([v[1],v[2]])
            g[v[1]].append([v[0],v[2]])
        res=inf
        travel=[0 for _ in range(0,n+1)]
        def dfs(x):
            nonlocal res
            travel[x]=1
            for y in g[x]:
                res=min(res,y[1])
                if travel[y[0]]==0:
                    dfs(y[0])
        dfs(1)
        return res
                
                


            
        