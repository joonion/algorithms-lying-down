#Kadane's Algorithm

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        for i in range(len(nums)):
            cursum = 0
            for j in range(i, len(nums)):
                cursum += nums[j]
                if cursum > maxsum:
                    maxsum = cursum
        return maxsum

s = Solution()
n = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
print(s.maxSubArray(n))



