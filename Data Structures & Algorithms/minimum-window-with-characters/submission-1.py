class Solution:
    def minWindow(self, s: str, t: str) -> str:
       count_t, window = {},{}
       for i in range(len(t)):
        count_t[t[i]] = 1 + count_t.get(t[i],0)
       need = len(count_t)
       have = 0
       l,r = 0,0
       min_len = float("inf")
       res = ""
       while r < len(s):
        window[s[r]] = 1 + window.get(s[r], 0)
        if s[r] in count_t and window[s[r]] == count_t[s[r]]:
            have +=1
        while have == need:
            if r-l+1 < min_len:
                min_len = r-l+1
                res = s[l:r+1]
            window[s[l]] -=1
            if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                have-=1
            l+=1        
        r+=1
       return res 