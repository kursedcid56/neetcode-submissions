class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r =len(height) -1
        res = 0
        max_left,max_right = 0,0
        while l <r:
            if height[l] < height[r]:
                if max_left > height[l]:
                    res += max_left - height[l]
                else:
                    max_left = height[l]  
                l+=1          
            else:
                if max_right > height[r]:
                    res += max_right - height[r]
                else:
                    max_right = height[r]    
                r-=1
        return res            