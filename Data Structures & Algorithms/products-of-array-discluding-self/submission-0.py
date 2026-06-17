class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # loop through the list and find multiplication of other numbers
        ret = []
        for idx,num in enumerate(nums):
            nw_arr = nums[0:idx]
            nw_arr.extend(nums[idx+1:])

            mlt = 1
            for n in nw_arr:
                mlt = (mlt * n)
            
            ret.append(mlt)
        return ret