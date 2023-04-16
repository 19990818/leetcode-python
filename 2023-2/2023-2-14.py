

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        m=dict()
        res,cnt=0,0
        for (i,v) in enumerate(hours):
            if v>8:
                cnt+=1
            else: cnt-=1
            if m.get(cnt) is None:
                m[cnt]=i
            if cnt>0:
                res=max(res,i+1)
            else:
                if m.get(cnt-1) is not None:
                    res=max(res,i-m[cnt-1])
        return res