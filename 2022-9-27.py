

class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        dic1,dic2=dict(),dict()
        for i in range(0,len(s1)):
            if dic1.get(s1[i]) is None:
                dic1.setdefault(s1[i],1)
            else:
                dic1[s1[i]]+=1
            if dic2.get(s2[i]) is None:
                dic2.setdefault(s2[i],1)
            else:
                dic2[s2[i]]+=1
        for k in dic1:
            if dic2.get(k) is None or dic2.get(k)!=dic1.get(k):
                return False
        return True
    
    
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dic1=[[] for i in range(0,n+1)]
        for dislike in dislikes:
            dic1[dislike[0]].append(dislike[1])
            dic1[dislike[1]].append(dislike[0])
        global color
        color=1
        travel=dict()
        def bfs(start)->bool:
            queue=[start]
            travel[start]=color
            while True:
                temp=[]
                color^=3
                while len(queue)>0:
                    cur=queue[0]
                    queue=queue[1:]
                    for child in dic1[cur]:
                        if travel.get(child) is not None and travel[child]!=color:
                            return False
                        if travel.get(child) is None:
                            travel[child]=1
                            temp.append(child)
                if len(temp)==0:
                    break
                queue=temp
        for i in range(1,n+1):
            if travel.get(i) is None and not bfs(i):
                return False
        return True
            
        