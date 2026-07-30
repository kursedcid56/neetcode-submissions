class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       l,r = 0,0
       contain = set()
       res = 0
       while r<len(s):
        if s[r] not in contain:
            contain.add(s[r])
            res = max(res, (r-l+1))
            r+=1
        else:
            l+=1
            contain.remove(s[l-1])
       return res         