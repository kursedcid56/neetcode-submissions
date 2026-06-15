class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       visited = {}
       for i,n in enumerate(nums):
        needed_num = target - n
        if needed_num in visited:
            return [visited[needed_num], i]

        visited[n] = i 

