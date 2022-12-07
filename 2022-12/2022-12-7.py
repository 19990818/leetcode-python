

from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1,sum2=sum(nums1),sum(nums2)
        nums1.sort()
        nums2.sort()
        diff=abs(sum1-sum2)
        if diff==0:return 0
        if sum1>sum2: nums1,nums2=nums2,nums1
        left,right=0,len(nums2)-1
        res=0
        while left<len(nums1) or right>=0:
            if right==-1 or (left<len(nums1) and nums1[left]+nums2[right]<7):
                diff-=(6-nums1[left])
                left+=1
            else:
                diff-=(nums2[right]-1)
                right-=1
            res+=1
            if diff<=0:return res
        return -1
    
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def findKthOdd(nums,idx):
            cnt=0
            for (i,num) in enumerate(nums):
                if num%2==1:cnt+=1
                if cnt==idx: return i
            return -1
        left,right=findKthOdd(nums,1),findKthOdd(nums,k)
        if right==-1:return 0
        lc,rc=left+1,1
        res=0
        while right<len(nums):
            right+=1
            while right<len(nums) and nums[right]%2==0:
                right+=1
                rc+=1
            res+=lc*rc
            lc,rc=1,1
            left+=1
            while left<len(nums) and nums[left]%2==0:
                left+=1
                lc+=1
        return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right  
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(r):
            res=[]
            def dfs(r):
                if r is None:
                    return res
                dfs(r.left)
                res.append(r.val)
                dfs(r.right)
            dfs(r)
            return res
        res1,res2=inorder(root1),inorder(root2)
        return sorted(res1+res2)
                