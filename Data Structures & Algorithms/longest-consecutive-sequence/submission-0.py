class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        longest = 0

        for n in num:
            if n - 1 not in num:
                current = n
                streak = 1
                while current + 1 in num:
                    current += 1
                    streak += 1
                longest = max(longest,streak)
        return longest