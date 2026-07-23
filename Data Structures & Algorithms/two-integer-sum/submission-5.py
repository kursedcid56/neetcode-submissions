class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       contain = {}
       for i, j in enumerate(nums):
        needed_num = target - j
        if needed_num in contain:
            return [contain[needed_num], i]
        contain[j] = i     
    





