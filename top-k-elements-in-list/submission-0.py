from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        visited = [False] * len(nums)
        freq = []

        # Step 1: count frequency
        for i in range(len(nums)):
            if visited[i]:
                continue

            count = 1

            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
                    visited[j] = True

            freq.append([nums[i], count])

        # Step 2: sort based on count (descending)
        freq.sort(key=lambda x: x[1], reverse=True)

        # Step 3: take top k
        result = []
        for i in range(k):
            result.append(freq[i][0])

        return result