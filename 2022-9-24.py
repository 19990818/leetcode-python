
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0]*len(code)
        ans = [0 for i in range(0,len(code))]
        if k>0:
            origin,i=0,1
            for _ in range(0,k):
                origin+=code[i]
                i=(i+1)%len(code)
            ans[0]=origin
            for j in range(1,len(code)):
                ans[j]=ans[j-1]+code[i]-code[j]
                i=(i+1)%len(code)
        else:
            origin,i=0,len(code)-1
            for _ in range(0,-k):
                origin+=code[i]
                i=(i-1+len(code))%len(code)
            ans[0]=origin
            for j in range(1,len(code)):
                i=(i+1)%len(code)
                ans[j]=ans[j-1]+code[j-1]-code[i]
        return ans