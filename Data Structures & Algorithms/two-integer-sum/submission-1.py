from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i in range(len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i] + nums[j]==target:
                    res.append(i)
                    res.append(j)
                else:
                    j+=1
            i+=1

        return res
            
       