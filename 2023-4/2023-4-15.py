class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        res=0
        diff=[0 for _ in range(0,len(reward1))]
        for i in range(0,len(reward1)):
            diff[i]=reward1[i]-reward2[i]
            res+=reward2[i]
        diff=sorted(diff,reverse=True)
        for i in range(0,k):
            res+=diff[i]
        return res
            
            