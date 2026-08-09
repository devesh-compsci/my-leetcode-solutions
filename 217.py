# Use Sets (dosen't allow duplicates | compare lengths)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        if len(set(nums)) == len(nums):
            return False
        else:
            return True
