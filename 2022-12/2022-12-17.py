from typing import List


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i,j=0,0
        while i<len(groups) and j<len(nums):
            temp=j
            for k in range(0,len(groups[i])):
                if j<len(nums) and nums[j]==groups[i][k]:
                    j+=1
            if j-temp == len(groups[i]):
                i+=1
            else:
                j=temp+1
        return i==len(groups)