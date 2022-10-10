

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        dp1,dp2=0,1
        for i in range(1,len(nums1)):
            a,b=10**9,10**9
            if nums1[i]>nums1[i-1] and nums2[i]>nums2[i-1]:
                a,b=min(a,dp1),min(b,dp2+1)
            if nums1[i]>nums2[i-1] and nums2[i]>nums1[i-1]:
                a,b=min(a,dp2),min(b,dp1+1)
            dp1,dp2=a,b
        return min(dp1,dp2)