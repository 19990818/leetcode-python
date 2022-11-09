
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        m=dict()
        for v in allowed:
            m[v]=1
        res=0
        for word in words:
            flag=1
            for c in word:
                if m.get(c) is None:
                    flag=0
                    break
            res+=flag
        return res