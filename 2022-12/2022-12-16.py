from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        sumNums=sum(nums)
        diff=abs(goal-sumNums)
        return (diff+limit-1)//limit

