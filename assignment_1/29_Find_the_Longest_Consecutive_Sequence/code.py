class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = list(sorted(set(nums)))
        longest = 0
        count = 1

        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                count += 1
            else:
                longest = max(longest, count)
                count = 1

        return max(longest, count)

input("Press any key to exit !")
