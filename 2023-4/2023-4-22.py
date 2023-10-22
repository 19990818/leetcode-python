from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        brother=defaultdict(int)
        q=[root]
        sumA=[root.val]
        while len(q)>0:
            temp=q
            q=[]
            sum=0
            while len(temp)>0:
                if temp[0].left is not None and temp[0].right is not None:
                    brother[temp[0].left]=temp[0].right.val
                    brother[temp[0].right]=temp[0].left.val
                if temp[0].left is not None:
                    q.append(temp[0].left)
                    sum+=temp[0].left.val
                if temp[0].right is not None:
                    q.append(temp[0].right)
                    sum+=temp[0].right.val
                temp[0].val=sumA[-1]-temp[0].val-brother[temp[0]]
                temp=temp[1:]
            sumA.append(sum)
        return root
    
    
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res=[0,0]
        for (i,v) in enumerate(mat):
            cnt=0
            for v2 in v:
                if v2==1:
                    cnt+=1
            if cnt>res[1]:
                res=[i,cnt]
        return res
    
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisors.sort()
        res=divisors[0]
        mcnt=0
        for d in divisors:
            cnt=0
            for n in nums:
                if n%d==0: cnt+=1
                if cnt>mcnt:
                    mcnt=cnt
                    res=d
        return res
    
    
class Solution:
    def addMinimum(self, word: str) -> int:
        cnt=1
        for i in range(1,len(word)):
            if word[i]<=word[i-1]:
                cnt+=1
        return cnt*3-len(word)
