

from bisect import bisect_left, bisect_right


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        startx,starty=0,0
        res=""
        for v in target:
            x,y=int(ord(v)-ord("a"))//5,int(ord(v)-ord('a'))%5
            if v=='z':
                res+=(y-starty)*'R'+(starty-y)*'L'+(x-startx)*'D'+(startx-x)*'U'
            else:
                res+=(x-startx)*'D'+(startx-x)*'U'+(y-starty)*'R'+(starty-y)*'L'
            startx,starty=x,y
            res+="!"
        return res
    

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res,cnt=0,0
        n=len(nums)
        for i in range(0,n):
            if cnt<n-1:
                temp=str(nums[i])+str(nums[n-1-i])
                res+=int(temp)
                cnt+=2
            elif cnt==n-1:
                cnt+=1
                res+=nums[i]
        return res
    

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res=0
        for (i,v) in enumerate(nums):
            l,r=bisect_left(nums,lower-v,i+1),bisect_right(nums,upper-v,i+1)
            res+=r-l
        return res
            