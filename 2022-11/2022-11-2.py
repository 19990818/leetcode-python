from math import sqrt


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        res,maxSum=[0,0],0
        for x in range(0,51):
            for y in range(0,51):
                temp=0
                for tower in towers:
                    dis=pow(x-tower[0],2)+pow(y-tower[1],2)
                    if dis<=pow(radius,2):
                        temp+=tower[2]//(sqrt(dis)+1)
                if temp>maxSum:
                    maxSum=temp
                    res[0],res[1]=x,y
        return res
