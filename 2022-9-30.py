

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




class Solution:
    def reformatNumber(self, number: str) -> str:
        number=number.replace("-","")
        number=number.replace(" ","")
        ans=""
        for i in range (0,len(number),3):
            if ans!="":
                ans+="-"
            if len(number)-i>4:
                ans+=number[i:i+3]
            elif len(number)-i==4:
                ans+=number[i:i+2]
                ans+="-"
                ans+=number[i+2:i+4]
                break
            else:
                ans+=number[i:]
                break
        return ans