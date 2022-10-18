class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        ans=0
        nstr=str(n)
        for i in range(1,len(nstr)): ans+=pow(len(digits),i)
        start=1
        m,less=dict(),dict()
        for i in range(0,digits.size()):
            while(start<=int(digits[i])):
                less[str(start)]=i
                start+=1
        while(start<=9):
            less[str(start)]=len(digits)
            start+=1
        for i in range(0,len(nstr)):
            if i>0 and m.get(nstr[i]) is None:
                break
            ans+=less[nstr[i]]*pow(len(digits),len(nstr)-i-1)
        def isExistSame() ->bool:
            for v in nstr:
                if m.get(v) is None:
                    return False
            return True
        if isExistSame():return ans+1
        return ans