class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rtary = [1]*len(nums)
        # forward loop
        prfx = 1
        for idx,num in enumerate(nums):
            rtary[idx] = prfx
            prfx *= num

        # backward loop
        bckwrd = 1
        for idx in range(len(nums)-1,-1,-1):
            rtary[idx] *= bckwrd
            bckwrd *= nums[idx]
        
        return rtary