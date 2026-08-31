class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        left = max(nums)    
        right = sum(nums)   


        while left <= right :
            mid= (left+right)//2
            current_sum = 0
            subarrays = 1
            sums=[]
            for num in nums:
                if current_sum + num <= mid:
                    current_sum += num
                else:
                    sums.append(current_sum)
                    subarrays += 1
                    current_sum = num
                sums.append(current_sum)


            if subarrays > k:
                left = mid + 1
            else:
                right = mid - 1

        return left