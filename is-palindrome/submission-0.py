class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        # Step 1: keep only letters and numbers, convert to lowercase
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        # Step 2: check palindrome using two pointers
        left = 0
        right = len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True