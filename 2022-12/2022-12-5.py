
from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        n=len(toppingCosts)
        res=baseCosts[0]
        def getClosestNum(a,b,t):
            if abs(a-t)<abs(b-t):return a
            if abs(a-t)==abs(b-t):return min(a,b)
            return b
        def dfs(cur,idx):
            nonlocal res
            res=getClosestNum(res,cur,target)
            if cur>target or idx==n:
                return
            dfs(cur,idx+1)
            dfs(cur+toppingCosts[idx],idx+1)
            dfs(cur+toppingCosts[idx]*2,idx+1)
        for v in baseCosts:
            dfs(v,0)
        return res



