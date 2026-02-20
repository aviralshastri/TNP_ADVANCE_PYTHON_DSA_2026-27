from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        def bs(nums, i, j):
            if i == j:
                return i

            m = (i + j) // 2

            if nums[m] < nums[m + 1]:
                return bs(nums, m + 1, j)
            else:
                return bs(nums, i, m)

        return bs(nums, 0, n - 1)

input("Press any key to exit !")
