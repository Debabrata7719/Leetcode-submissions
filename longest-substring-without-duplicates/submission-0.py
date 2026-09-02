class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = ""
        max_len = 0

        for ch in s:

            while ch in window:
                window = window[1:]

            window += ch

            max_len = max(max_len, len(window))

        return max_len