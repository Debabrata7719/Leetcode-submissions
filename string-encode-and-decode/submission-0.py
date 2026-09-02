from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        
        for s in strs:
            encoded += str(len(s)) + "#" + s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # Step 1: find length
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            
            # Step 2: extract string
            i = j + 1
            word = s[i:i + length]
            res.append(word)
            
            # Step 3: move pointer
            i = i + length

        return res
    
