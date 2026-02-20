class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k=k%n
        temp=nums[n-k:n:]
        remaining=nums[:n-k:]
        nums[:] = temp + remaining
        return nums

input("Press any key to exit !")
