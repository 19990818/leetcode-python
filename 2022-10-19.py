

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt1,cnt0=0,0
        for stu in students:
            if stu==1:cnt1+=1
            else:cnt0+=1
        for saw in sandwiches:
            if saw==1:cnt1-=1
            else:cnt0-=1
            if cnt0<0 or cnt1<0:break
        return max(cnt1,cnt0)
    
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        pairs=[]
        for i in range(0,len(values)):
            pairs.append((values[i],labels[i]))
        pairs=sorted(pairs,key=lambda x:x[0])
        ans=0
        cnt=dict()
        pairs.reverse()
        print(pairs)
        for pair in pairs:
            if cnt.get(pair[1]) is None or cnt[pair[1]]<useLimit:
                if cnt.get(pair[1]) is None:
                    cnt[pair[1]]=1
                else:
                    cnt[pair[1]]+=1
                numWanted-=1
                ans+=pair[0]
            if numWanted<=0:
                break
        return ans
    
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        if grid[0][0]==1 or grid[-1][-1]==1: return -1
        travel=dict()
        travel[0]=1
        cnt=1
        queue=[0]
        tos=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        while True:
            temp=[]
            while len(queue)>0:
                cur=queue[0]
                if cur==m*n-1:
                    return cnt
                queue=queue[1:]
                x,y=cur//n,cur%n
                for to in tos:
                    if x+to[0]>=0 and x+to[0]<m and y+to[1]<n and y+to[1]>=0 and grid[x+to[0]][y+to[1]]==0 and travel.get((x+to[0])*n+y+to[1]) is None:
                        travel[(x+to[0])*n+y+to[1]]=1
                        temp.append((x+to[0])*n+y+to[1])
            if len(temp)==0:break
            queue=temp
            cnt+=1
        return -1

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans=[label]
        while label>1:
            label=label//2
            sum=(1<<label.bit_length())*3-1
            ans.append(sum-label)
            label=sum-label
        return ans.reverse()

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:return 0
        if k<=(1<<(n-2)): return self.kthGrammar(n-1,k)
        return 1-self.kthGrammar(n-1,k-(1<<(n-2)))