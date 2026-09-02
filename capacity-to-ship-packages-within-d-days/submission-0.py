class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left= max(weights)
        right= sum(weights)
        ans=right
        
        while left <= right :
            mid =(left+right)//2
            day_used=1
            current_weight=0
            
            for weight in weights:
                if current_weight+weight <= mid:
                    current_weight+=weight
                else:
                    day_used +=1
                    current_weight = weight
            if day_used <= days:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return ans