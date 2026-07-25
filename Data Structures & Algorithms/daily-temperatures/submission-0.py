from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []          # stores indices
        ans = [0] * len(temperatures)

        i = 0

        while i < len(temperatures):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev

            stack.append(i)
            i += 1

        return ans