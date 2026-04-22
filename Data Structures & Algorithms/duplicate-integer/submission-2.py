class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = list(set(nums))
        if len(num) == len(nums):
            return False
        else:
            return True