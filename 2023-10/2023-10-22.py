
from ast import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sum=0
        res=0
        satisfaction.sort()
        for i in range(len(satisfaction)-1,-1,-1):
            sum+=satisfaction[i]
            if sum>=0:
                res+=sum
            else:
                break
        return res
    
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        res=0
        j=0
        for i in range(len(tasks)-1,-1,-4):
            res=max(res,processorTime[j]+tasks[i])
            j+=1
        return res
    
class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        res=[]
        s=[]
        cnt=0
        for v in words:
            if v=="prev":
                cnt+=1
                if cnt>len(s):
                    res.append(-1)
                else:
                    res.append(int(s[len(s)-cnt]))
            else:
                s.append(v)
                cnt=0
        return res
    
class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        s=[0]
        for i in range(1,len(groups)):
            if groups[i]!=groups[s[-1]]:
                s.append(i)
        res=[0 for _ in range(0,len(s))]
        for i in range(0,len(s)):
            res[i]=words[s[i]]
        return res
    
class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        def getNext(s):
            res=[]
            template="abcdefghijklmnopqrstuvwxyz"
            for i in range(0,len(s)):
                for v in template:
                    if v!=s[i]:
                        res.append(s[0:i]+v+s[i+1:])
            return res
        m=dict()
        cnt=1
        m[words[0]]=[0]
        for i in range(1,len(words)):
            m[words[i]]=[]
            for v in getNext(words[i]):
                if m.get(v) is not None and groups[m.get(v)[-1]]!=groups[i] and len(m[words[i]])<len(m.get(v)):
                    m[words[i]]=[val for val in m.get(v)]
            m[words[i]].append(i)
            cnt=max(cnt,len(m[words[i]]))
        res=[]
        for k in m:
            if len(m[k])==cnt:
                for v in m[k]:
                    res.append(words[v])
                break
        return res

                    