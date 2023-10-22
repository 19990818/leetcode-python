


from collections import defaultdict


class Solution:
    def trap(self, height: List[int]) -> int:
        mv,idx=height[0],0
        for (i,v) in enumerate(height):
            if (v>mv):
                mv,idx=v,i
        def getSum(start,step):
            if start==idx:
                return 0
            temp,cidx=height[start],start
            i=start+step
            ans=0
            while i<len(height) and i>=0:
                if height[i]>=temp:
                    ans+=temp*(abs(cidx-i)-1)
                    temp=height[i]
                    cidx=i
                else:
                    ans-=height[i]
                if i==idx:break
                i+=step
            return ans
        return getSum(0,1)+getSum(len(height)-1,-1)
    
    
    
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        m=defaultdict(int)
        for v in nums:
            m[v]+=1
        nmc,cnt=nums[0],m[nums[0]]
        for v in m:
            if m[v]>cnt:
                nmc,cnt=v,m[v]
        cnt=0
        for i in range(0,len(nums)):
            if nums[i]==nmc:
                cnt+=1
            if 2*cnt>(i+1) and 2*(m[nmc]-cnt)>len(nums)-i-1:
                return i
        return -1
    
    
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return False
        m=defaultdict(int)
        for num in nums:
            m[num]+=1
        for i in range(1,len(nums)):
            if i<len(nums)-1 and m[i]==1:
                continue
            if i==len(nums)-1 and m[i]==2:
                continue
            return False
        return True
    
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        temp=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<=temp:
                temp+=nums[i]
            else:
                temp=nums[i]
        return temp
        
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels="AEIOUaeiou"
        idxs=[]
        vstrs=[]
        strs=[]
        for i in range(0,len(s)):
            if vowels.find(s[i]) != -1:
                idxs.append(i)
                vstrs.append(s[i])
            strs.append(s[i])
        vstrs.sort()
        i=0
        for idx in idxs:
            strs[idx]=vstrs[i]
            i+=1
        return "".join(strs)