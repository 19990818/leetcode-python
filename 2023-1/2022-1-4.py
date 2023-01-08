class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left,right=1,maxSum+1
        while left+1<right:
            mid=(left+right)>>1
            sum=mid
            if index>=mid-1:
                sum+=mid*(mid-1)//2+(index-mid+1)
            else:
                sum+=(2*mid-1-index)*index//2
            if n-index>=mid:
                sum+=mid*(mid-1)//2+(n-index-mid)
            else:
                sum+=(mid+mid-n+index)*(n-1-index)//2
            if sum<=maxSum: left=mid
            else: right=mid
        return left
    
class Solution:
    def countEven(self, num: int) -> int:
        def isEven(n:int):
            sum=0
            while n>0:
                sum+=n%10
                n=n//10
            return sum%2==0
        res=0
        for i in range(1,num+1):
            if isEven(i):
                res+=1
        return res