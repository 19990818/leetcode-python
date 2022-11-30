

class Solution:
    def minOperations(self, s: str) -> int:
        res1,res2=0,0
        temp1,temp2="0","1"
        for v in s:
            if v==temp1:res2+=1
            else: res1+=1
            temp1,temp2=temp2,temp1
        return min(res1,res2)