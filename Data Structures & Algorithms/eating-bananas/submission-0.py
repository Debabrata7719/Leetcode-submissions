class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right = max(piles)
        k=(left+right)//2
        ans=right
        while left <= right :
            hours=0
            k= (right+left)//2
            for pile in piles:
                hours += (pile + k - 1) // k

            if hours <= h:
                ans = k
                right = k - 1
            else:
                left = k + 1

        return ans