from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        m=defaultdict(int)
        for i in range(0,len(order)):
            m[order[i]]=i
        return "".join(sorted(list(s),key=lambda val:m[val]))