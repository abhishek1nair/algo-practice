# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                # making 4 swaps to reach correct position
                # key insight will be recieved if you use the indices
                # of the matrix and try to come up with a formula for the
                # swap positions. For this case the formula is:
                # (i, j) -> (j, m-i) -> (m-i, m-j) -> (m-j, i)
                # m here is the max index i.e., len(matrix) - 1 
                matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i] = \
                    matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]


# Test the solution
s = Solution()

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

# expected output
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

# expected output
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]


s.rotate(matrix)

print(matrix)
