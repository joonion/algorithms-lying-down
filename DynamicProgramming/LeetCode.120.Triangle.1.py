from typing import List

def solve(row, col, triangle):
    if row == len(triangle):
        return 0
    else:
        return triangle[row][col] + \
               min(solve(row + 1, col, triangle), \
                   solve(row + 1, col + 1, triangle))

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return solve(0, 0, triangle)

s = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(s.minimumTotal(triangle))
