class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if lengths are same
        if len(s)!=len(t):
            return False
        # create a hashmap
        count_s = {}
        count_t = {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i],0)
            count_t[t[i]] = 1 + count_t.get(t[i],0)
        for j in count_s:
            if count_s[j] != count_t.get(j,0):
                return False
        return True
