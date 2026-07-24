class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new = sorted(nums)
        res = []
        for i in range(len(new)):
            if i > 0 and  new[i-1] == new[i]:
                continue
            C = new[i]
            l = i+1
            r = len(new) -1
            while l < r:
                if new[l] + new[r] == -C:
                    res.append([C,new[l],new[r]])
                    l+=1
                    r-=1
                    while l < r and new[l] == new[l-1]:
                        l+=1
                    while l < r and new[r] == new[r+1]:
                        r-=1    
                elif new[l] + new[r] > -C:    
                    r -=1
                elif new[l] + new[r] < -C:
                    l +=1   
        return res         