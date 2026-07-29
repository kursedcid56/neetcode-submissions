class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contain = set()
        res = 0
        l,r = 0,0
        while r < len(s):
            if s[r] not in contain:
                contain.add(s[r])
                res = max(res, r-l+1)
                r+=1
            else:
                contain.remove(s[l])        
                l+=1
                
        return res            