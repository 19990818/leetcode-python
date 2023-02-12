from collections import defaultdict


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        cur,start,cnt=n-2,n-2,0
        while cur!=start or cnt==0:
            if cur%2==0:
                cur=cur//2
            else:
                cur=n//2+cur//2
            cnt+=1
        return cnt
    
class Solution:
    def digitCount(self, num: str) -> bool:
        m=defaultdict(int)
        for n in num:
            m[int(n)]+=1
        # print(m)
        for (i,n) in enumerate(num):
            # print(i,n)
            if m[i]!=int(n):
                return False
        return True