class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) -1
        while l < r:
            tong = int(numbers[l] + numbers[r])
            if tong == target:
                return [l+1,r+1]
            elif tong > target:
                r-=1
            elif tong < target:
                l+=1        
          

            