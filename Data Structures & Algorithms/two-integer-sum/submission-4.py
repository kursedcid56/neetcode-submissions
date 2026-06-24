class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       visited = {}
       for i,j in enumerate(nums):
        needed_num = target - j
        if needed_num in visited:
            return [visited[needed_num], i]

        visited[j] = i


