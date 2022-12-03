from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res=[0 for _ in range(0,len(boxes))]
        pre=self.getCost(boxes)
        temp="".join(reversed(boxes))
        post=self.getCost(temp)
        for i in range(1,len(pre)):
            res[i-1]=pre[i]+post[-i]
        return res
    def getCost(self,s: str)->List[int]:
        sum=0
        dp=[0 for _ in range(0,len(s)+1)]
        for i in range(0,len(s)):
            dp[i+1]=dp[i]+sum
            if s[i]=="1": sum+=1
        return dp