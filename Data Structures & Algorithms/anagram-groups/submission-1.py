from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # solve using hash map
        group_anagram = defaultdict(list)
        for word in strs:
            # count all 26 letters for each word
            count = [0]*26
            for ltr in word:
                count[ord(ltr)-ord("a")] += 1
            group_anagram[tuple(count)].append(word)
        return list(group_anagram.values())