class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        min_length = float("inf")
        while left < len(nums):

            current_sum = 0

            # Calculate sum of current window
            for i in range(left, right + 1):
                current_sum += nums[i]

            if current_sum >= target:
                min_length = min(min_length, right - left + 1)
                left += 1
            else:
                if right < len(nums) - 1:
                    right += 1
                else:
                    break

        if min_length == float("inf"):
            return 0
            
        return min_length
                