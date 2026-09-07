class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        original = len(nums)
        s = set(nums)
        if original == len(s):
            return False
        else:
            return True
        