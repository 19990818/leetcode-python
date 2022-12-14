from typing import List


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parent=[i for i in range(0,n)]
        index=[i for i in range(0,len(queries))]
        res=[False for _ in range(0,len(queries))]
        edgeList.sort(key=lambda x: x[2])
        index.sort(key=lambda x:queries[x][2])
        def findParent(a):
            if parent[a]==a:return a
            parent[a]=findParent(parent[a])
            return parent[a]
        def merge(a,b):
            pa,pb=findParent(a),findParent(b)
            parent[pa]=pb
        j=0
        for i in index:
            while j<len(edgeList) and edgeList[j][2]<queries[i][2]:
                merge(edgeList[j][0],edgeList[j][1])
                j+=1
            res[i]=findParent(queries[i][0])==findParent(queries[i][1])
        return res
        