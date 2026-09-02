class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalin(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Try skipping LEFT char OR skipping RIGHT char
                return isPalin(left + 1, right) or isPalin(left, right - 1)
            left += 1
            right -= 1
        
        return True