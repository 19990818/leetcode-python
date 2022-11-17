class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        m=dict()
        for i in range(0,len(nums)):
            m[nums[i]]=i
        cur=m[0]
        for i in range(1,len(nums)):
            if cur-m[i]>1:return False
            cur=max(cur,m[i])
        return True