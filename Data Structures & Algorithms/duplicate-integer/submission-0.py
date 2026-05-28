class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # loop through list
        for idx,num in enumerate(nums):
            if num in nums[idx+1:]:
                return True
        return False
        