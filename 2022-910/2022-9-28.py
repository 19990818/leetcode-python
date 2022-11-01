

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        if k==1:
            return 1
        queue=[1]
        tp,fp,sp=0,0,0
        for _ in range(0,k):
            temp=min(3*queue[tp],5*queue[fp])
            temp=min(temp,7*queue[sp])
            if 3*queue[tp]==temp:
                tp+=1
            if 5*queue[fp]==temp:
                fp+=1
            if 7*queue[sp]==temp:
                sp+=1
            queue.append(temp)
        return queue[-1]
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        i=1
        while(i<len(preorder)):
            if preorder[i]==postorder[-2]:
                break
            i+=1
        root=TreeNode(preorder[0])
        root.left=self.constructFromPrePost(preorder[1:i],postorder[0:i-1])
        root.right=self.constructFromPrePost(preorder[i:],postorder[i-1:-1])
        return root
    
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        m=dict()
        m[arr[0]]=1
        for i in range(1,len(arr)):
            m[arr[i]]=1
            j=i-1
            while j>=0 and (arr[j]|arr[i])!=arr[j]:
                arr[j]|=arr[i]
                m[arr[j]]=1
                j-=1
        return len(m)

