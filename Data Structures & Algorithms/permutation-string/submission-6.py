class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      l,r = 0,0
      count_s1 = {}
      count_s2 = {}
      for i in range(len(s1)):
        count_s1[s1[i]]  = count_s1.get(s1[i], 0) +1 
      while r < len(s2):
        count_s2[s2[r]] = 1 + count_s2.get(s2[r], 0) 
        if r-l+1 > len(s1):
            count_s2[s2[l]] -=1
            if count_s2[s2[l]] == 0:
                del count_s2[s2[l]]
            l+=1
        if count_s1 == count_s2:
            return True
        r+=1
      return False            
