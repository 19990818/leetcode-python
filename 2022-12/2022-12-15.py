class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def strSum(s):
            res=0
            for c in s:
                res+=int(c)
            return str(res)
        def getNumStr(s):
            res=""
            for c in s:
                res+=str(ord(c)-ord('a')+1)
            return res
        src=getNumStr(s)
        for i in range(0,k):
            src=strSum(src)
        return int(src)
        