class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(a):
            if a==1:
                return False
            i=2
            while i*i<=a:
                if a%i==0:
                    return False
                i+=1
            return True
        res=0
        for i in range(0,len(nums)):
            for j in range(0,len(nums[i])):
                if i==j or j==len(nums)-i-1:
                    if isPrime(nums[i][j]):
                        res=max(res,nums[i][j])
        return res
    
    
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        res=[0 for _ in range(0,len(nums))]
        m=dict()
        for (i,v) in enumerate(nums):
            if  m.get(v) is None:
                m[v]=[i]
            else:
                m[v].append(i)
        for k in m:
            sum=[0 for _ in range(0,len(m[k])+1)]
            total=0
            for idx in  m[k]:
                total+=idx
            for (i,idx) in enumerate(m[k]):
                sum[i+1]=sum[i]+idx
                res[idx]=idx*i-sum[i]+total-sum[i]-idx*(len(m[k])-i)
        return res
            