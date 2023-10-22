from ast import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted(intervals,key=lambda x:x[1])
        res=[]
        start,end=intervals[0][0],intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=end or i==len(intervals)-1:
                start=min(intervals[i][0],start)
                end=max(intervals[i][1],end)
            else:
                res.append([start,end])
                start,end=intervals[i][0],intervals[i][1]
        return res
    
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left,right=0,0
        for c in moves:
            if c=='R':
                right,left=right+1,left-1
            elif c=='L':
                right,left=right-1,left+1
            else:
                right,left=right+1,left+1 
        return max(left,right)
        
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        res=0
        i=1
        cnt=0
        m=dict()
        while cnt<n:
            if m.get(target-i) is None:
                cnt+=1
                res+=i
                m[i]=1
            i+=1
        return res