class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left  = 0
        right = len(heights) - 1
        ans = 0
        while left < right:
            b = right - left
            curr_area = b * min(heights[left],heights[right])
            ans = max(curr_area,ans)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return ans