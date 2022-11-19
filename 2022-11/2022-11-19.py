from typing import List, Optional


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res,temp=0,0
        for v in gain:
            temp+=v
            res=max(res,temp)
        return res
    
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        p=[0 for _ in range(0,len(nums))]
        p[0]=1
        mod=10**9+7
        for i in range(1,len(nums)):
            p[i]=(p[i-1]*2)%mod
        res=0
        for i in range(0,len(nums)):
            res=(res+(p[i]-p[len(nums)-i-1])*nums[i]%mod)%mod
        return res
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q=[root]
        ans=0
        while len(q)>0:
            temp=q
            q=[]
            a=[0 for _ in range(0,len(temp))]
            id=[0 for _ in range(0,len(temp))]
            for i,v in enumerate(temp):
                a[i]=v.val
                id[i]=i
                if v.left is not None:
                    q.append(v.left)
                if v.right is not None:
                    q.append(v.right)
            # print(a,id)
            id.sort(key=lambda x:a[x])
            vis=[False for _ in range(0,len(temp))]
            ans+=len(temp)
            for i in range(0,len(temp)):
                if not vis[i]:
                    p=i
                    while not vis[p]:
                        vis[p]=True
                        p=id[p]
                    ans-=1
        return ans
            