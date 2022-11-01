
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        m=dict()
        i,j,ans=0,0,0
        while i<=j and j<len(fruits):
            while True:
                if m.get(fruits[j]) is None:
                    m[fruits[j]]=1
                else:
                    m[fruits[j]]+=1
                j+=1
                if len(m)>2:break
                if j==len(fruits):
                    j+=1
                    break
            ans=max(ans,j-i-1)
            while len(m)>2:
                m[fruits[i]]-=1
                if m[fruits[i]]==0:m.pop(fruits[i])
                i+=1
        return ans