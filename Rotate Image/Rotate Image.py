class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        i=0
        j=i+1
        while i<n-1:
            for m in range(i+1,n):
                matrix[i][m],matrix[m][i]=matrix[m][i],matrix[i][m]
            i+=1
            j=i+1
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-j-1]=matrix[i][n-j-1],matrix[i][j]
        
