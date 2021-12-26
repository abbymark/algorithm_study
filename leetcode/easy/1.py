from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    nums_sorted = sorted(nums)

    start = 0
    end = len(nums) -1

    while True:
        num_sum = nums_sorted[start] + nums_sorted[end]
        if num_sum == target:
            first_index = nums.index(nums_sorted[start])
            nums[first_index] = -1
            
            return [first_index, nums.index(nums_sorted[end])]        
        
        if num_sum < target:
            start += 1
            continue
        else:
            end -= 1


print(twoSum(nums = [2,7,11,15], target = 9))
print(twoSum(nums = [3,3], target = 6))