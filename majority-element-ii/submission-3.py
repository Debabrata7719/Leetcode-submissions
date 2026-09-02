class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        result = []
        n = len(nums)

        # count frequency
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # check > n/3
        for key in count:
            if count[key] > n // 3:
                result.append(key)

        return result