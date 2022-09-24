class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        m=dict()
        for i in range(0,len(arr)):
            m[arr[i]]=i
        for i in range(0,len(pieces)):
            if m.get(pieces[i][0]) is None:
                return False
            for j in range(1,len(pieces[i])):
                if m.get(pieces[i][j]) is None or m.get(pieces[i][j-1]) is None:
                    return False
                if m.get(pieces[i][j])!=m.get(pieces[i][j-1])+1:
                    return False
        return True

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        same,diff=[[0 for i in range(len(t)+1)] for i in range(len(s)+1)],[[0 for i in range(len(t)+1)] for i in range(len(s)+1)]
        ans=0
        for i in range(0,len(s)):
            for j in range(0,len(t)):
                if s[i]==t[j]:
                    same[i+1][j+1]=same[i][j]+1
                    diff[i+1][j+1]=diff[i][j]
                else:
                    diff[i+1][j+1]=same[i][j]+1
                ans+=diff[i+1][j+1]
        return ans

            