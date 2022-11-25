from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        res=0
        des=self.trans(s)
        for word in words:
            src=self.trans(word)
            # print(des,src)
            if len(src)!=len(des):
                break
            flag=True
            for i in range(0,len(src)):
                if not (src[i][0]==des[i][0] and (src[i][1]==des[i][1] or des[i][1]>2) and des[i][1]>=src[i][1]):
                    flag=False
            if flag: res+=1
        return res
    def trans(self,s)->list[list]:
        temp=s[0]
        s=s+"0"
        cnt=0
        res=[]
        for v in s:
            if v==temp:
                cnt+=1
            else:
                res.append([temp,cnt])
                # res+=[temp,cnt]
                temp,cnt=v,1
        return res
    
    
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n=len(edges)+1
        g=[[] for _ in range(0,n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        bobTime=[n]*n
        def dfsBob(c,p,t) -> bool:
            if c==0:
                bobTime[c]=t
                return True
            for y in g[c]:
                if y!=p and dfsBob(y,c,t+1):
                    bobTime[c]=t
                    return True
            return False
        dfsBob(bob,-1,0)
        # print(bobTime,g)
        g[0].append(-1)
        res=-inf
        def dfsAlice(c,p,t,total):
            if t<bobTime[c]:
                total+=amount[c]
            elif t==bobTime[c]:
                total+=amount[c]/2
            if len(g[c])==1:
                nonlocal res
                res=max(res,total)
                return
            for y in g[c]:
                if y!=p:
                    dfsAlice(y,c,t+1,total)
        dfsAlice(0,-1,0,0)
        return int(res)
        