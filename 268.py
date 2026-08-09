class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        return sum(range(len(nums)+1)) - sum(nums)
