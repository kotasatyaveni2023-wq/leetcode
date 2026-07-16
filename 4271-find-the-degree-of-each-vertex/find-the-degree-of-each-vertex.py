class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n=len(matrix)
        res=[]
        for row in matrix:
            s=sum(row)
            res.append(s)
        return res
        