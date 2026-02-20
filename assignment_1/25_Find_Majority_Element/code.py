class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        half_n = len(nums) // 2
        for num, count in freq.items():
            if count > half_n:
                return num

input("Press any key to exit !")
