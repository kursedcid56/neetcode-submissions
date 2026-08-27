class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       contain = {}
       for i in range(len(nums)):
        needed_num = target - nums[i]
        if needed_num in contain:
            return [contain[needed_num], i]
        contain[nums[i]] = i    





