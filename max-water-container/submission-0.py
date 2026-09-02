class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            
            # Step 1: calculate height
            h = min(heights[left], heights[right])
            
            # Step 2: calculate gap
            width = right - left
            
            # Step 3: calculate area
            area = h * width
            
            # Step 4: update max area
            max_area = max(max_area, area)
            
            # Step 5: move pointer (IMPORTANT)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area