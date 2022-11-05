class Solution:
    def reachNumber(self, target: int) -> int:
        target=abs(target)
        sum,i=0,1
        while(True):
            sum+=i
            if sum>=target:
                if (sum-target)%2==0:
                    return i
                if (sum+i+1-target)%2==0:
                    return i+1
                return i+2
            i+=1
        return -1