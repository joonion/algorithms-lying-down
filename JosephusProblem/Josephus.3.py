# Josephus Problem:
#   LeetCode 1823. Find the Winner of the Circular Game

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        return ((self.findTheWinner(n - 1, k) + k - 1) % n) + 1

s = Solution()
print(s.findTheWinner(41, 3))