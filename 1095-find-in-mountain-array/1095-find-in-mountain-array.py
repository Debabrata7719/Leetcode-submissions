class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        # COACH: Current Time Complexity: O(log N) | Space Complexity: O(1)
        # Optimal Complexity: O(log N) | Space Complexity: O(1)
        
        # BUG 1: In LeetCode's MountainArray interface, you must use mountainArr.get(index) 
        # and mountainArr.length() is a method, not a property.
        n = mountainArr.length()
        left=0
        right=n-1
        #finding Peak
        while left < right:
            mid=(left+right)//2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        
        # BUG 2: The peak assignment and subsequent binary searches were inside 
        # the first while loop. They must be outside to run AFTER the peak is found.
        peak = left

        left=0
        right=peak
        #Increasing order
        while left <= right:
            mid=(left+right)//2

            value = mountainArr.get(mid)

            if value == target:
                return mid
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        #decreasing Order
        left=peak+1
        right=n-1

        while left <=right:
            mid=(left+right)//2

            value=mountainArr.get(mid)

            if value==target:
                return mid

            elif value > target :
                left =mid+1
            else:
                right =mid-1
                
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna