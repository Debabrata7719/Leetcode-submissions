class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0:
            return []

        res = []

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                current_sum = numbers[i] + numbers[j]

                if current_sum == target:
                    res.append(i + 1)   # 1-based index
                    res.append(j + 1)
                    return res

        return res