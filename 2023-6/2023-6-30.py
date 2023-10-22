

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        m=dict()
        res=0
        for word in words:
            temp=""
            for c in word:
                temp=c+temp
            if m.get(temp) !=None:
                res+=1
            m[word]=1
        return res
    
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        return 4*min(x,y)+2*z+2*min(z,1,abs(x-y))