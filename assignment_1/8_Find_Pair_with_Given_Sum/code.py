class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i,v in enumerate(nums):
            difference=target-v

            if hash_map.get(difference,None)!=None:
                return [i,hash_map[difference]]
            hash_map[v]=i

input("Press any key to exit !")
