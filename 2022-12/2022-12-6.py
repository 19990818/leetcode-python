
from collections import defaultdict


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        m=defaultdict(int)
        temp,flag=0,0
        res=0
        word+="a"
        for c in word:
           if c.isdigit():
               temp=temp*10+int(c)
               flag=1
               continue
           elif m[temp]==0 and flag==1:
               m[temp]=1
               res+=1
               temp,flag=0,0
           else:temp,flag=0,0 
        return res