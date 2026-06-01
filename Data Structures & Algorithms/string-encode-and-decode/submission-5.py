import ast
class Solution:

    def encode(self, strs: List[str]) -> str:
        jnt_strs = ""
        for st in strs:
            nstr = str(len(st)) + "#" + st
            jnt_strs +=nstr
        return jnt_strs
        

    def decode(self, s: str) -> List[str]:
        strs,i = [],0
        while i < len(s):
            j = i # need to some operations on j to find out hash
            while s[j] != "#":
                j+=1
            wrd_lnt = int(s[i:j])
            wrd = s[j+1:j+1+wrd_lnt]
            strs.append(wrd)
            i = j + wrd_lnt + 1
        
        return strs