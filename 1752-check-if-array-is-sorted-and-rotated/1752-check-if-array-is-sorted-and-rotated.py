class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sortedN=sorted(nums)
        result=True

        for i in range(len(nums)-1,-1,-1):
            rotated = nums[i:] + nums[:i]

            if rotated == sortedN:
                return True
        
        return False
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna