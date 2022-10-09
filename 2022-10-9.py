class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        a=[]
        res=0
        for i in s:
            if i=='(':a.append(i)
            else:
                temp,part=1,0
                while(a[-1]!='('):
                    part+=a[-1]
                    a=a[0:-1]
                if part!=0: temp=2*part
                a=a[0:-1]
                a.append(temp)
        while len(a)>0:
            res+=a[-1]
            a=a[0:-1]
        return res
    
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans=0
        for i in range(1,min(a,b)+1):
            if a%i==0 and b%i==0: ans+=1
        return ans


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans=0
        m,n=len(grid),len(grid[0])
        for i in range(1,m-1):
            for j in range(1,n-1):
                temp=grid[i][j]
                tos=[[-1,-1],[-1,0],[-1,1],[1,-1],[1,0],[1,1]]
                for to in tos: temp+=grid[i+to[0]][j+to[1]]
                ans=max(ans,temp)
        return ans
    

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt=0
        for i in range(0,32):
            if num2&1<<i: cnt+=1
        a=[0 for _ in range(0,32)]
        i=31
        while(i>=0 and cnt>0):
            if num1&1<<i:
                a[i]=1
                cnt-=1
            i-=1
        i=0
        while(i<32 and cnt>0):
            if a[i]==0:
                a[i]=1
                cnt-=1
            i+=1
        ans=0
        for i in range(0,32):
            if a[i]==1:ans+=1<<i
        return ans
                