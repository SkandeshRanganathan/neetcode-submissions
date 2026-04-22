class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            comp = target - num
            if comp not in seen:
                seen[num] = i
            else:
                return [seen[comp] , i]