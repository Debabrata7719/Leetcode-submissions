from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []

        for ch in operations:
            if ch == "+":
                s.append(s[-1] + s[-2])
        
            elif ch == "D":
                s.append(2 * s[-1])
        
            elif ch == "C":
                s.pop()
        
            else:
                s.append(int(ch))

        return sum(s)
       
        