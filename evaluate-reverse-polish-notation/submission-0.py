from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)

            elif ch == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)

            elif ch == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)

            elif ch == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))  # Truncate toward zero

            else:
                stack.append(int(ch))

        return stack.pop()