class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count_n = {}
       for i in nums:
        count_n[i] = 1 + count_n.get(i,0)
       count_n = sorted(count_n,key=count_n.get,reverse = True)
       return list(count_n[:k])


    