class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # prepare a hashmap of the frequency
        freqCount = {}
        for idx,num in enumerate(nums):
            freqCount[num] = 1 + freqCount.get(num,0)
        sortedList = sorted(freqCount.items(),key= lambda x:x[1],reverse=True)
        return [i[0] for i in sortedList[0:k]]