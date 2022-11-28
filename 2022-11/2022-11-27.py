

class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        for i in range(0,n):
            flag=True
            for j in range(1,n):
                if nums[(j+i)%n]<nums[(j+i-1)%n]:
                    flag=False
                    break
            if flag: return True
        return False