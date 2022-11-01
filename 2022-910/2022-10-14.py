

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        cnt=[0 for _ in range(0,26)]
        mod=10**9+7
        for c in s:
            temp=1
            for i in range(0,26):
                temp=(temp+cnt[i])%mod
            cnt[ord(c)-ord('a')]=temp
        ans=0
        for i in range(0,26):
            ans=(ans+cnt[i])%mod
        return ans
    
    
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        pos=0
        for i in range(1,n+1):
            ans.append("Push")
            if target[pos]!=i:ans.append("Pop")
            else:pos+=1
            if pos==len(target):break
        return ans