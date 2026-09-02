class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range (len(nums)):
            sum=nums[i]
            for j in range(i + 1, len(nums)):
                second = nums[j]

                if sum + second == target:
                    return [i ,j]
                 

            
        