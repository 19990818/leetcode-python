from collections import Counter, defaultdict
from typing import List


class FreqStack:

    def __init__(self):
        self.cnt=Counter()
        self.stacks=[]


    def push(self, val: int) -> None:
        if self.cnt[val]==len(self.stacks):
            self.stacks.append([val])
        else:
            self.stacks[self.cnt[val]].append(val)
        self.cnt[val]+=1

    def pop(self) -> int:
        res=self.stacks[-1][-1]
        self.stacks[-1]=self.stacks[-1][0:-1]
        if len(self.stacks[-1])==0:
            self.stacks=self.stacks[0:-1]
        self.cnt[res]-=1
        return res
    
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp=[0 for _ in range(0,3)]
        res=0
        show=defaultdict(int)
        show[0]=1
        for num in nums:
            o=num%3
            temp=[dp[i] for i in range(0,len(dp))]
            for i in range(0,3):
                if show[(i-o+3)%3]==1:
                    dp[i]=max(temp[i],temp[(i-o+3)%3]+num)
            show[o]=1
            for j in range(0,len(dp)):
                if dp[j]!=0:
                    show[j]=1
            # print(dp)
            res=max(res,dp[0])
        return res


            
        
        
        