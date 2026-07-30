class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        contain = {}
        res = 0 
        while r< len(s):
            contain[s[r]] = 1 + contain.get(s[r],0)
            while (r-l+1) - max(contain.values()) > k:
                contain[s[l]] -=1
                l +=1
            res = max (res, r-l+1)
            r+=1
        return res        