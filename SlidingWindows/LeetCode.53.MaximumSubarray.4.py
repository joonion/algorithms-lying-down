#Kadane's Algorithm

from typing import List

def max_to_left(mid, low, S):
    lmax, lsum = S[mid], 0
    for i in range(mid, low - 1, -1):
        lsum += S[i]
        lmax = max(lmax, lsum)
    return lmax

def max_to_right(mid, high, S):
    rmax, rsum = S[mid], 0
    for i in range(mid, high + 1):
        rsum += S[i]
        rmax = max(rmax, rsum)
    return rmax

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            mid = len(nums) // 2
            print(nums[:mid], nums[mid:])
            lmax = max_to_left(mid - 1, 0, nums)
            rmax = max_to_right(mid, len(nums) - 1, nums)
            print(lmax, rmax, lmax + rmax)
            return max(lmax + rmax, \
                       self.maxSubArray(nums[:mid]), \
                       self.maxSubArray(nums[mid:]))

s = Solution()
# n = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
n = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(n))