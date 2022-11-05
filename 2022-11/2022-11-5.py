class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if expression=='t':return True
        if expression=='f':return False
        exps=self.splitEpr(expression[2:-1])
        return self.solution(exps,expression)

    def solution(self,exps,exp)->bool:
        res=self.parseBoolExpr(exps[0])
        if exp[0]=='|':
            for i in range(1,len(exps)):
                res=res or self.parseBoolExpr(exps[i])
            return res
        if exp[0]=='&':
            for i in range(1,len(exps)):
                res=res and self.parseBoolExpr(exps[i])
            return res
        return not res
    def splitEpr(self,expr)->list:
        expr+=','
        cnt=0
        res,temp=[],[]
        for i in range(0,len(expr)):
            if expr[i]=='(':cnt+=1
            elif expr[i]==')':cnt-=1
            elif cnt==0 and expr[i]==',':
                res.append("".join(temp))
                temp=[]
                continue
            temp.append(expr[i])
        # print(res)
        return res
    
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        dp=[[0 for _ in range(0,n+1)] for _ in range(0,n+1)]
        sum=[0 for _ in range(0,n+1)]
        for i in range(len(piles)-1,-1,-1):
            sum[i]=sum[i+1]+piles[i]
        # print(sum)
        for i in range(1,n+1):
            dp[n-1][i]=piles[n-1]
            dp[n][i]=0
        for i in range(n-2,-1,-1):
            # print("i ",i)
            for j in range(1,n+1):
                for x in range(1,n-i+1):
                    if 1<=x and x<=j:
                        dp[i][j]=max(dp[i][j],sum[i]-dp[i+x][j])
                    elif x>j and x<=2*j:
                        dp[i][j]=max(dp[i][j],sum[i]-dp[i+x][x])
        # print(dp)
        return dp[0][1] 
    
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
            arrx,arry=[1],[1]
            m=dict()
            res=[]
            if x>1: arrx=self.getSmallerBound(x,bound)
            if y>1: arry=self.getSmallerBound(y,bound)
            for x in arrx:
                for y in arry:
                    if m.get(x+y) is None and x+y<=bound:
                        res.append(x+y)
                        m[x+y]=1
            return res
            
    def getSmallerBound(self,t,bound)->list:
        temp=1
        res=[]
        while temp<=bound:
            res.append(temp)
            temp*=t
        return res