class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0
        r = 0
        #count frequncy of each character in t
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}

        min_len = float('inf')
        start = 0

        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1

            valid = True
            #comapre window with required character
            for ch in need:
                if window.get(ch, 0) < need[ch]:
                    valid = False
                    break
            #slide window and check again
            while valid:
                curr_len = r - l + 1
                if curr_len < min_len:
                    min_len = curr_len
                    start = l

                window[s[l]] -= 1
                l += 1

                valid = True
                for ch in need:
                    if window.get(ch, 0) < need[ch]:
                        valid = False
                        break

            r += 1

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]