

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        i=0
        while i<len(word1) and i<len(word2):
            ans+=word1[i]
            ans+=word2[i]
            i+=1
        ans+=word1[i:]
        ans+=word2[i:]
        return ans


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        a,b=[0 for _ in(0,len(nums))],[0 for _ in(0,len(nums))]
        a[0],b[-1]=nums[0],nums[-1]
        for i in range(1,len(nums)):
            a[i]=max(a[i-1],nums[i])
        for i in range(len(nums)-2,0,-1):
            b[i]=min(b[i+1],nums[i])
        for i in range(0,len(nums)-1):
            if a[i]<=b[i+1]:
                return i+1
        return -1
    
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        a,b=dict(),dict()
        for trip in trips:
            if a.get(trip[1]) is None:
                a[trip[1]]=trip[0]
            else: a[trip[1]]+=trip[0]
            if b.get(trip[2]) is None:
                b[trip[2]]=trip[0]
            else: b[trip[2]]+=trip[0]
        sum=0
        for i in range(0,1001):
            if a.get(i) is not None:
                sum+=a[i]
            if b.get(i) is not None:
                sum-=b[i]
            if sum>capacity:return False
        return True
    
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        highest=pow(10,n-1)
        m=dict()
        ans=[]
        def dfs(node:int ):
            for i in range(0,k):
                if m.get(node*10+i) is None:
                    m[node*10+i]=1
                    dfs((node*10+i)%highest)
                    ans.append(str(i))
        dfs(0)
        return "".join(ans)+"0"*(n-1)