class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        
#        if len(nums) == 2:
#            return [0,1]   
        seen = {}

        for i,x in enumerate(nums):
            needed = target - x

            if needed in seen:
                return [seen[needed], i]

            seen[x] = i
