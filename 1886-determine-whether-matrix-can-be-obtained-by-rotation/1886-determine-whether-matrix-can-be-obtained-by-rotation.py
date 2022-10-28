class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        
        for i in range(3):
            self.rotate(mat)
            if mat == target:
                return True
        return False

    def swap(self, matrix, i, j, i1, j1):
        tmp = matrix[i][j]
        matrix[i][j] = matrix[i1][j1]
        matrix[i1][j1] = tmp
    
    def rotate(self, matrix):
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            for j in range(C//2):
                self.swap(matrix, i, j, i, C - j - 1)
        # print(f"{matrix}")
        for i in range(R):
            for j in range(i + 1, C):
                self.swap(matrix, i, j, j, i)
        # print(f"rotated: {matrix}")