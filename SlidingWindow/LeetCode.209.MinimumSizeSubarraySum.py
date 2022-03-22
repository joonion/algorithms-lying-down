from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = len(nums)
        start, current = 0, 0
        for i in range(len(nums)):
            current += nums[i]
            if current >= target:
                if minimum > i - start + 1:
                    minimum = i - start + 1
                start, current = i, nums[i]
        return minimum

sol = Solution()
target, nums = 7, [2, 3, 1, 2, 4, 3]
print(sol.minSubArrayLen(target, nums))
