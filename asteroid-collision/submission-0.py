from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:

            # Check for collisions
            while stack and stack[-1] > 0 and asteroid < 0:

                # Current asteroid is bigger
                if abs(asteroid) > abs(stack[-1]):
                    stack.pop()

                # Both are equal
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                    break

                # Stack asteroid is bigger
                else:
                    break

            else:
                stack.append(asteroid)

        return stack