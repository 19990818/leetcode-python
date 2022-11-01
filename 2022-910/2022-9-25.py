

class Solution:
    def rotatedDigits(self, n: int) -> int:
        def isRotatedDigits(n)->bool:
            dic1={0:1,1:1,2:1,5:1,6:1,8:1,9:1}
            dic2={2:1,5:1,6:1,9:1}
            nstr=str(n)
            flag=False
            for b in nstr:
                if dic1.get(int(b)-int('0')) is None:
                    return False
                if dic2.get(int(b)-int('0')) is not None:
                    flag=True
            return flag
        ans=0
        for i in range(2,n+1):
            if isRotatedDigits(i):
                ans+=1
        return ans
    
    
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        m=dict()
        ans=0
        for obstacle in obstacles:
            m[(obstacle[0],obstacle[1])]=1
        dx,dy=[0,1,0,-1],[1,0,-1,0]
        x,y,status=0,0,0
        for command in commands:
            if command==-1:
                status=(status+1)%4
            elif command==-2:
                status=(status+3)%4
            else:
                for i in range(0,command):
                    if m.get((x+dx[status],y+dy[status])) is not None:
                        break
                    x+=dx[status]
                    y+=dy[status]
                ans=max(ans,x*x+y*y)
        return ans
        