from typing import List

MIN = -(10 ** 4) - 1

def solve(row, col, triangle, cost):
    if row == len(triangle):
        return 0
    elif cost[row][col] == MIN:
        cost[row][col] = triangle[row][col] + \
                         min(solve(row + 1, col, triangle, cost), \
                             solve(row + 1, col + 1, triangle, cost))
    return cost[row][col]

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cost = [[MIN for j in range(len(triangle[i]))] for i in range(len(triangle))]
        return solve(0, 0, triangle, cost)

s = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(s.minimumTotal(triangle))