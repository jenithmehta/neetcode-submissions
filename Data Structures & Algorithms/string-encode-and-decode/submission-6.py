import ast
class Solution:

    def encode(self, strs: List[str]) -> str:
        jnt_strs = ""
        for st in strs:
            jnt_strs +=str(len(st)) + "#" + st
        return jnt_strs
        

    def decode(self, s: str) -> List[str]:
        strs,i = [],0
        while i < len(s):
            j = i # need to some operations on j to find out hash
            while s[j] != "#":
                j+=1
            wrd_lnt = int(s[i:j])
            strs.append(s[j+1:j+1+wrd_lnt])
            i = j + wrd_lnt + 1
        
        return strs