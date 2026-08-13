class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
         l,r = 0,0
         max_len = 0
         count_s = {}
         while r < len(s):
            count_s[s[r]] = 1 + count_s.get(s[r], 0)
            max_freq = max(count_s.values())
            while (r-l+1) - max_freq > k:
                l+=1
                count_s[s[l-1]] -=1
            max_len = max(max_len,r-l+1) 
            r+=1
         return max_len      

