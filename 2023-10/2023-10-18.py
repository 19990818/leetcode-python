from queue import PriorityQueue
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        q=PriorityQueue()
        for num in nums:
            q.put(-num)
        res = 0
        for i in range(0,k):
            cur = q.get()
            res-=cur
            q.put(-((-cur+2)//3))
        return res