class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        freq = {}
        max_freq = 0
        result = 0

        while right < len(s):
            # Add current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Update maximum frequency
            max_freq = max(max_freq, freq[s[right]])

            # Current window size
            window_length = right - left + 1

            # If window is invalid, shrink it
            if window_length - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # Update the answer
            result = max(result, right - left + 1)

            # Expand the window
            right += 1

        return result