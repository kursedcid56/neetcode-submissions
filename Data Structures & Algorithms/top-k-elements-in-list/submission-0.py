class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_num = {}
        for i in range(len(nums)):
            count_num[nums[i]] = 1 + count_num.get(nums[i], 0)
        rs = sorted(count_num, key=count_num.get, reverse=True) 
        return rs[:k]