
from ast import List
import bisect
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d=defaultdict(list)
        res=0
        for i,c in enumerate(s):
            d[c].append(i)
        for word in words:
            cur,ok=-1,True
            for c in word:
                j=bisect.bisect_right(d[c],cur)
                if j==len(d[c]):
                    ok=False
                    break
                cur=d[c][j]
            if ok: res+=1
        return res
        