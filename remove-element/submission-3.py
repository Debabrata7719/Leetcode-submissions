class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=[]
        for i in range (len(nums)):
            if nums[i]==val:
                continue
            k.append(nums[i])
        nums[:] = k
        return len(nums)