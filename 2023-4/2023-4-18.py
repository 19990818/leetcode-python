class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfs(r: Optional[TreeNode]):
            nonlocal res
            if r is None:
                return
            ma1,mi1,ma2,mi2=r.val,r.val,r.val,r.val
            if r.left is not None:
                t1,t2=dfs(r.left)
                ma1=max(ma1,t1)
                mi1=min(mi1,t2)
            if r.right is not None:
                t1,t2=dfs(r.right)
                ma2=max(ma2,t1)
                mi2=min(mi2,t2)
            ma=max(ma1,ma2)
            mi=min(mi1,mi2)
            res=max(res,max(abs(ma-r.val),abs(mi-r.val)))
            return ma,mi
        dfs(root)
        return res
        