class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        c=self.gcd(a,b)
        mod=10**9+7
        lgm=a*b/c
        left,right=1,10**15
        while left<right:
            mid=(left+right)//2
            if mid//a+mid//b-mid//lgm<n:
                left=mid+1
            else:
                right=mid
        return left%mod
    def gcd(self,a,b) -> int:
        while b>0:
            a,b=b,a%b
        return a