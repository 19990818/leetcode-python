
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def cntInCir(x,y):
            return pow(x-xCenter,2)+pow(y-yCenter,2)<=radius*radius
        if xCenter<=x2 and xCenter>=x1 and yCenter>=y1 and yCenter<=y2:
            return True
        if xCenter<=x2 and xCenter>=x1:
            return abs(yCenter-y1)<=radius or abs(yCenter-y2)<=radius
        if yCenter<=y2 and yCenter>=y1:
            return abs(xCenter-x1)<=radius or abs(xCenter-x2)<=radius
        return cntInCir(x1,y1) or cntInCir(x1,y2) or cntInCir(x2,y1) or cntInCir(x2,y2)