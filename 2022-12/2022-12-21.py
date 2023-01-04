from collections import defaultdict
from typing import List


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        return min((a+b+c)//2,a+b+c-max(a,b,c))

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res=0
        for op in operations:
            if op=="X++" or op=="++X":
                res+=1
            else:
                res-=1
        return res
    
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res=""
        while word1!='' and word2!='':
            if word1<word2:
                res+=word2[0]
                word2=word2[1:]
            else:
                res+=word1[0]
                word1=word1[1:]
        res+=word1+word2
        return res
    
class Solution:
    def minimumBoxes(self, n: int) -> int:
        i,j,cur=1,1,1
        while n>cur:
            n-=cur
            i+=1
            cur+=i
        cur=1
        while n>cur:
            n-=cur
            j+=1
            cur+=1
        return i*(i-1)//2+j
    
class Solution:
    def countHomogenous(self, s: str) -> int:
        mod=10**9+7
        temp=s[0]
        cnt=0
        s+='A'
        res=0
        for v in s:
            if v==temp:
                cnt+=1
            else:
                res=(res+cnt*(cnt+1)/2)%mod
                temp=v
                cnt=1
        return res
    
class Solution:
    def minimumMoves(self, s: str) -> int:
        res=0
        i=0
        while i<len(s):
            if s[i]=='X':
                res+=1
                i+=2
            i+=1
        return res



class Solution:
    def captureForts(self, forts: List[int]) -> int:
        def cntNum(start,step):
            res,cnt=0,0
            flag=False
            while start>=0 and start<len(forts):
                if forts[start]==1:
                    flag=True
                    cnt=0
                if forts[start]==0 and flag:
                    cnt+=1
                if forts[start]==-1:
                    res=max(res,cnt)
                    cnt=0
                    flag=False
                start+=step
            return res
        return max(cntNum(0,1),cntNum(len(forts)-1,-1))
    
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        m=defaultdict(int)
        add,sub=-3,1
        for v in positive_feedback: m[v]=add
        for v in negative_feedback: m[v]=sub
        grades=[]
        i=0
        for rq in report:
            words=rq.split(" ")
            grade=0
            for word in words: grade+=m[word]
            grades.append([grade,student_id[i]])
            i+=1
        grades.sort()
        return [grades[i][1] for i in range(0,k)]


class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def lcm(a,b):
            sum=a*b
            while b>0:
                a,b=b,a%b
            return sum/a
        def check(k):
            cnt1,cnt2,cnt3=k//divisor1,k//divisor2,k//lcm(divisor1,divisor2)
            both=k-cnt1-cnt2+cnt3
            forArr1=cnt2-cnt3
            forArr2=cnt1-cnt3
            return max(uniqueCnt1-forArr1,0)+max(uniqueCnt2-forArr2,0)<=both
        left,right=1,2*10**9
        # right=mid left<right<mid 那么left+right//2肯定不会再等于mid 就不会有死循环
        # 而如果left=mid right=mid+1的话 left+right//2可能等于mid造成死循环
        while left<right:
            mid=(left+right)//2
            if check(mid):right=mid
            else:   left=mid+1
        return left
    
class Solution:
    def minimumLength(self, s: str) -> int:
        
        start,end=0,len(s)-1
        while start<end and s[start]==s[end]:
            i=start
            while i<len(s) and s[i]==s[start]: i+=1
            j=end
            while j>=0 and s[j]==s[end]:j-=1
            start,end=i,j
        return max(end-start+1,0)


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res=-1
        n=len(words)
        for i in range(0,n):
            if words[(i+startIndex)%n]==target:
                if res==-1:
                    res=min(i,n-i)
                else:
                    res=min(res,min(i,n-i))
        return res
    
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        full=defaultdict(int)
        if k==0: return 0
        n=len(s)
        s+=s
        i,j=0,0
        cnt=[0,0,0]
        res=-1
        while i<n and j<len(s):
            while (len(full)<3 and j<len(s)) or (i!=0 and j<n):
                cnt[int(ord(s[j])-ord('a'))]+=1
                if cnt[int(ord(s[j])-ord('a'))]>=k:
                    full[s[j]]=1
                j+=1
            if len(full)==3 and (i==0 or j>=n) and j-i<=n:
                if res==-1:
                    res=j-i
                else: res=min(res,j-i)
            cnt[int(ord(s[i])-ord('a'))]-=1
            if cnt[int(ord(s[i])-ord('a'))]<k and full[s[i]]!=0:
                del full[s[i]]
            i+=1
        return res