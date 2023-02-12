

from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        end=0
        coins.sort()
        for v in coins:
            if v>end+1:
                break
            end+=v
        return end+1