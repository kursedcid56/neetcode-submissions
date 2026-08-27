class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       contain = {}
       for i,n in enumerate(nums):
        needed_num = target - n
        if needed_num in contain:
            return [contain[needed_num], i]
        contain[n] = i    





