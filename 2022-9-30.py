

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        dicx,dicy=dict(),dict()
        for  i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j]==0:
                    dicx[i],dicy[j]=0,0
        for k in dicx:
            for j in range(0,len(matrix[0])):
                matrix[k][j]=0
        for k in dicy:
            for i in range(0,len(matrix)):
                matrix[i][k]=0