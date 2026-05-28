class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = list(s)
        tl = list(t)
        sl.sort()
        tl.sort()
        if sl == tl:
            return True
        return False