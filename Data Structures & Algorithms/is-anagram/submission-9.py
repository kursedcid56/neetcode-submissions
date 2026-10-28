class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        containS = {}    
        containT = {}    
        for i in range(len(s)):
            containS[s[i]] = 1 + containS.get(s[i],0)
            containT[t[i]] = 1 + containT.get(t[i],0)
        if containS == containT:
            return True
        return False        



        

