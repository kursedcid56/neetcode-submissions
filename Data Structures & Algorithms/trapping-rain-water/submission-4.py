class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r =len(height) -1
        res = 0
        while l < r:
            max_height = min(height[l],height[r])
            if height[l]< height[r]:
                water_contain = max_height - height[l]
                l+=1
            else:
                water_contain = max_height-height[r]    
                r-=1
            res += water_contain
        return res        