class Solution:
    def threeSum(self, nums):
        nums.sort()  # Step 1: sort the array
        res = []

        for i in range(len(nums)):
            # Step 2: skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 3: two pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # Step 4: skip duplicates for left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Step 5: skip duplicates for right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # move both pointers
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1  # need bigger sum
                else:
                    right -= 1  # need smaller sum

        return res