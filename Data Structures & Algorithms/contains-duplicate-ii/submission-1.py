from typing import List 

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate = False
        window=[]
        for i in range (len(nums)):
            if nums[i] in window:
                duplicate=True

            window.append(nums[i])
            if len(window) > k:
                window.pop(0)
            
        return duplicate