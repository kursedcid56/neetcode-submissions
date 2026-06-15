class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            needed_num =  target - nums[i]
            if needed_num  in visited:
               return [visited[needed_num], i]
            visited[nums[i]] = i


