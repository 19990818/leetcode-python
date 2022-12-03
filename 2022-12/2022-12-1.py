from cmath import inf
from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dis=inf
        res=-1
        i=0
        for point in points:
            if point[0]==x or point[1]==y:
                if (point[0]-x)**2+(point[1]-y)**2<dis:
                    dis=(point[0]-x)**2+(point[1]-y)**2
                    res=i
            i+=1
        return res
        