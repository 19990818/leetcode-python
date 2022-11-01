from bisect import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs=sorted(zip(startTime,endTime,profit),key=lambda x:x[1])
        n=len(startTime)
        endTime=sorted(endTime)
        dp=[0 for _ in range(0,n)]
        dp[0]=jobs[0][2]
        for i in range(1,n):
            if jobs[i][0]>=endTime[i-1]:
                dp[i]=dp[i-1]+jobs[i][2]
            else:
                j=bisect(endTime,jobs[i][0])
                if jobs[i][0]!=endTime[j]:j-=1
                if j>=0:dp[i]=max(dp[j]+jobs[i][2],dp[i-1])
                else: dp[i]=max(jobs[i][2],dp[i-1])
        return dp[-1]
        