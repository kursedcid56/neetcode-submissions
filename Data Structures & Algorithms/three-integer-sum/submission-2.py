class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i,j  in enumerate(nums):
            if i > 0 and j  == nums[i-1]:
                continue
            l = i +1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == -j:
                    res.append([j,nums[l],nums[r]])
                    l +=1
                    r -=1    
                    while l<r and nums[l] == nums[l-1]:
                        l +=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                elif nums[l] + nums[r] < -j:
                    l+=1
                elif nums[l] + nums[r] > -j:
                    r-=1        

        return res               