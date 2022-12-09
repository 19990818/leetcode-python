
from typing import List, Optional


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        l=16
        pow3=[0 for _ in range(0,l)]
        pow3[0]=1
        for i in range(1,l):
            pow3[i]=pow3[i-1]*3
        for i in range(l-1,-1,-1):
            if n>=pow3[i]:
                n-=pow3[i]
                if n==0:
                    return True
        return False
    
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks=[]
        for a in arr:
            mask=0
            for c in a:
                if mask&(1<<(ord(c)-ord('a')))==0:
                    mask|=(1<<(ord(c)-ord('a')))
                else:
                    mask=0
                    break
            masks.append(mask)
        ans=0
        def dfs(pos,mask):
            if pos==len(masks):
                nonlocal ans
                ans=max(ans,bin(mask).count("1"))
                return
            if mask&masks[pos]==0:
                dfs(pos+1,mask|masks[pos])
            dfs(pos+1,mask)
        dfs(0,0)
        return ans  

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right  
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q=[root]
        res=root.val
        while len(q)>0:
            temp=q
            q=[]
            tempRes=0
            while len(temp)>0:
                cur=temp[0]
                temp=temp[1:]
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
                tempRes+=cur.val
            res=tempRes
        return res
        
        