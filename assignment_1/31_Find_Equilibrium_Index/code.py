array=[1,2,3,5,1,3,2]

def find_equilibrium_index(nums):
    total_sum = sum(nums)
    left_sum = 0
    
    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]
        
        if left_sum == right_sum:
            return i
        
        left_sum += nums[i]
    
    return -1


if __name__=="__main__":
    print(findEquilibriumIndex(array))

input("Press any key to exit !")
