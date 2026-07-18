from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_num=[]
        l=0
        r=k-1
        while r < len(nums):
            window_max=max(nums[l:r+1])
            max_num.append(window_max)

            l+=1
            r+=1

        return max_num
