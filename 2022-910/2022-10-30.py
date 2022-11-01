from curses.ascii import isupper


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[]
        temp=[ s[i] for i in range(0,len(s))]
        def dfs(i,temp):
            if i==len(s):
                res.append("".join(temp))
                return
            if s[i].islower():
                temp[i]=s[i].upper()
                dfs(i+1,temp)
                temp[i]=s[i]
            elif s[i].isupper():
                temp[i]=s[i].lower()
                dfs(i+1,temp)
                temp[i]=s[i]
            dfs(i+1,temp)
        dfs(0,temp)
        return res
    
    
class Solution:
    def magicalString(self, n: int) -> int:
        if n==1: return 1
        res,ans=0,[0 for _ in range(0,n)]
        ans[0]=1
        cur=1
        j=0
        i=0
        while i<n:
            count=ans[j]
            if ans[j]==0: count=cur
            while i<n and count>0:
                if cur==1:
                    res+=1
                ans[i]=cur
                i+=1
                count-=1
            cur^=3
            j+=1
        return res
        