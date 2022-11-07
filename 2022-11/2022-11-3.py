


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans=0
        for i in range(1,len(sequence)//len(word)+1):
            temp=i*word
            if sequence.find(temp)!=-1: ans=i
        return ans