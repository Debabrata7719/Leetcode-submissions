class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = 0
        want = len(needle)
        give = len(haystack)

        for i in range(give - want + 1):
            left = i
            right = i + want
            result = haystack[left:right]

            if result == needle:
                return i

        return -1