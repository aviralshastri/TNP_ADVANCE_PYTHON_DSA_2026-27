class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for ind,val in enumerate(nums):
            if ind!=val:
                return (val-1)
        return len(nums)

input("Press any key to exit !")
