from cmath import inf


class Solution:
    res=inf
    def kSimilarity(self, s1: str, s2: str) -> int:
        arr1,arr2=[],[]
        for x,y in zip(s1,s2):
            arr1=arr1.append(arr1,x)
            arr2=arr2.append(arr2,y)
        dfs(arr1,arr2,0,0)
        return res
    def dfs(self,s1,s2,cur,curans):
        if curans>res:
            return
        if s1==s2:
            res=curans
            return
        if s1[cur]==s2[cur]:
            dfs(s1,s2,cur+1,curans)
        else:
            for i in range (cur+1,len(s1)):
                if s1[i]!=s2[i] and s1[i]==s2[cur]:
                    s1[i],s2[i]=s2[i],s1[i]
                    dfs(s1,s2,cur+1,curans+1)
                    s1[i],s2[i]=s2[i],s1[i]