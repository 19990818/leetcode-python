from collections import defaultdict
from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        m=defaultdict(str)
        for v in knowledge:
            m[v[0]]=v[1]
        temp,res="",""
        inPa=False
        def getV(a):
            if m[a]=="":
                return "?"
            return m[a]
        for c in s:
            if c=='(':
                inPa=True
                temp=""
            elif c==')':
                res+=getV(temp)
                inPa=False
            elif inPa:
                temp+=c
            else:
                res+=c
        return res