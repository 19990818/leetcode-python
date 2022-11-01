import string


class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        s1=s1+s1
        return s1.find(s2)!=-1
    
class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.arr=[]
        self.cnt=[]
        for i in range(0,len(encoding),2):
            self.arr.append(encoding[i+1])
            self.cnt.append(encoding[i])

    def next(self, n: int) -> int:
        #print(self.arr,self.cnt)
        ans=-1
        while n>0 and len(self.cnt)>0:
            if self.cnt[0]>=n:
                self.cnt[0]-=n
                n=0
                ans=self.arr[0]
            else:
                n-=self.cnt[0]
                self.cnt[0]=0
            if self.cnt[0]==0:
                self.cnt=self.cnt[1:]
                self.arr=self.arr[1:]
        return ans

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num2=[]
        for i in range(len(nums1)):
            num2.append((i,nums2[i]))
        num2=sorted(num2,key=lambda x:x[1])
        nums1.sort()
        #print(num2,nums1)
        i,j=len(nums1)-1,len(nums1)-1
        ans=[-1 for _ in range(len(nums1))]
        while i>=0:
            while i>=0 and nums1[j]<=num2[i][1]:
                i-=1
            if i<0:
                break
            ans[num2[i][0]]=nums1[j]
            i-=1
            j-=1
        for k in range(0,len(nums1)):
            if ans[k]==-1:
                ans[k]=nums1[j]
                j-=1
        return ans
        