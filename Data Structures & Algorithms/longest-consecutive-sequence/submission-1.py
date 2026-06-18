class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # defining constant
        max_len = 0
        # lets loop through the nums
        for num in nums:
            seq_len = 1
            while True:
                num +=1
                if num in nums:
                    seq_len +=1
                else:
                    break
            max_len = max(max_len,seq_len)
        return max_len