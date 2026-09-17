class Solution:
    def minimumPairRemoval(self, nums):
        count = 0

        while any(nums[i] > nums[i + 1] for i in range(len(nums) - 1)):

            min_sum = float('inf')
            min_index = 0

            for i in range(len(nums) - 1):
                curr_sum = nums[i] + nums[i + 1]

                if curr_sum < min_sum:
                    min_sum = curr_sum
                    min_index = i

            nums[min_index] = nums[min_index] + nums[min_index + 1]
            nums.pop(min_index + 1)

            count += 1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna