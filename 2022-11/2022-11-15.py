from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sorted(boxTypes,key=lambda x:boxTypes[x][1])
        boxTypes.sort(key=lambda x:x[1])
        res=0
        for i in range(len(boxTypes)-1,-1,-1):
            if boxTypes[i][0]<=truckSize:
                res+=boxTypes[i][0]*boxTypes[i][1]
                truckSize-=boxTypes[i][0]
            else:
                res+=truckSize*boxTypes[i][1]
                truckSize=0
            if truckSize==0:
                return res
        return res