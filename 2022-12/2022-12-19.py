from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent=[i for i in range(0,n)]
        def findParent(a):
            if parent[a]==a:return a
            parent[a]=findParent(parent[a])
            return parent[a]
        def merge(a,b):
            pa=findParent(a)
            pb=findParent(b)
            parent[pa]=pb
        for edge in edges:
            merge(edge[0],edge[1])
        return findParent(source)==findParent(destination)