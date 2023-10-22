from ast import List


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        for i in range(0,len(nums)):
            if s[i]=="R":
                nums[i]+=d
            else:
                nums[i]-=d
        nums=sorted(nums)
        sum=0
        res=0
        mod = 1e9+7
        for i in range(0,len(nums)):
            res=(res+i*nums[i]-sum)%mod
            sum=(sum+nums[i])%mod
        return res
    
    
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)
        if prices[0]+prices[1]>money:
            return money
        return money-prices[0]-prices[1]