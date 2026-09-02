class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left_max, right_max = 0,0
        res = 0
        while l < r:
            if height[l] < height[r]:
                if left_max > height[l]:
                    res += left_max - height[l]
                    l+=1
                else:
                    left_max = height[l]
                    l+=1    
            else:
                if right_max> height[r]:
                    res  += right_max - height[r]
                    r-=1
                else:
                    right_max = height[r]
                    r-=1
        return res





















