from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = -1
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count = 0
            else:
                count += 1
            if longest < count:
                longest = count
        return longest

sol = Solution()
lin = [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1]
print(sol.findMaxConsecutiveOnes(lin))
       