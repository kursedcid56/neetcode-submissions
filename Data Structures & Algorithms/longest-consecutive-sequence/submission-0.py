class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in nums:
            if (i-1) not in numSet:
                leng = 1
                while (i+leng) in numSet:
                    leng += 1
                longest = max(longest,leng)

        return longest                
        