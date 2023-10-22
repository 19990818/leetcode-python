
primes=[]
mx = int(1e6)
np=[False]*(mx+1)
for i in range(2,mx+1):
    if not np[i]:
        primes.append(i)
        for j in range(i,int(mx/i)+1):
            np[i*j]=True


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        res = []
        if n%2==1:
            if n>4 and not np[n-2]:
                return [[2,n-2]]
            return []
        for x in primes:
            if x > n-x:
                break
            if not np[n-x]:
                res.append([x,n-x])
        return res