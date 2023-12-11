"""
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]


"""

class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        
        
matrix = [[1,2,3],[4,5,6],[7,8,9]]

x = Solution()
print(x.transpose(matrix))