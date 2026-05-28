class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through nums
        for idx,num in enumerate(nums):
            k = target - num
            if k in nums[idx+1:]:
                k_idx =  nums[idx+1:].index(k) + (idx+1)
                return [idx,k_idx]