

from string import ascii_lowercase
from typing import Counter


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        m=dict()
        for num in nums:m[num]=1
        flag=0
        while head!=None:
            if m.get(head.val) is None:
                flag=0
            elif  m.get(head.val)==1 and flag==0:
                flag=1
                ans+=1
        return ans
    
    
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ans,temp=logs[0][0],logs[0][1]
        for i in range(1,len(logs)):
            if logs[i][1]-logs[i-1][1]>temp:
                temp=logs[i][1]-logs[i-1][1]
                ans=logs[i][0]
            elif logs[i][1]-logs[i-1][1]==temp:
                ans=min(logs[i][0],ans)
        return ans
    
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans=[0 for _ in range(0,len(pref))]
        ans[0]=pref[0]
        for i in range(1,len(pref)):
            ans[i]=pref[i]^pref[i-1]
        return ans
    
    
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        mod=10**9+7
        dp=[[[0 for _ in range(0,k)]for _ in range(0,n+1)]for _ in range(0,m+1)]
        dp[1][0][0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                for x in range(0,k):
                    dp[i][j][(x+grid[i-1][j-1])%k]=(dp[i][j][(x+grid[i-1][j-1])%k]+dp[i][j-1][x]+
                                                    dp[i-1][j][x])%mod
        return dp[m][n][0]
    
class Solution:
    def robotWithString(self, s: str) -> str:
        cnt=Counter(s)
        ans=[]
        min=0
        st=[]
        for c in s:
            st.append(c)
            cnt[c]-=1
            while min<25 and cnt[ascii_lowercase[min]]==0:
                min+=1
            while len(st)>0 and st[-1]<=ascii_lowercase[min]:
                ans.append(st.pop())
        while len(st)>0:
            ans.append(st.pop())
        return "".join(ans)


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans,temp=0,0
        for i in range(0,len(arr)):
            for j in range(i,len(arr)):
                if arr[j]<arr[i]:temp=max(temp,j)
            if i==temp:
                ans+=1
                temp+=1
        return ans