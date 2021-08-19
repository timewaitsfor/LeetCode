import numpy as np


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        matrix = np.array(matrix)
        (m, n) = matrix.shape

        if target < matrix[0, 0] or target > matrix[-1, -1]:
            return False

        if m%2 == 0:
            mid_m = m//2 - 1
        else:
            mid_m = m // 2

        if n%2 == 0:
            mid_n = n//2 - 1
        else:
            mid_n = n // 2

        if target < matrix[mid_m][mid_n]:
            if mid_m != 0 and mid_n != 0:
                return self.searchMatrix(matrix[:mid_m, :], target) or self.searchMatrix(matrix[mid_m:, :mid_n], target)
            elif mid_n == 0:
                return self.searchMatrix(matrix[:mid_m, :], target)
            else:
                return self.searchMatrix(matrix[:, :mid_n], target)
        elif target > matrix[mid_m][mid_n]:
                if mid_m != m-1 and mid_n != n-1:
                    return self.searchMatrix(matrix[mid_m + 1:, :], target) or self.searchMatrix(
                        matrix[:mid_m+1, mid_n+1:], target)
                elif mid_n == n-1:
                    return self.searchMatrix(matrix[mid_m + 1:, :], target)
                else:
                    return self.searchMatrix(matrix[:, mid_n+1:], target)
        else:
            return True


solution = Solution()
M = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
k = 5
res = solution.searchMatrix(M, k)
print(res)