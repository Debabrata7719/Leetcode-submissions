
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        # Pair each position with its speed
        cars = list(zip(position, speed))

        # Sort cars by position in descending order (closest to target first)
        cars.sort(reverse=True)

        stack = []

        # Calculate time for each car to reach the target
        for pos, spd in cars:
            time = (target - pos) / spd

            # If the current car cannot catch the fleet ahead,
            # it forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)

            # Otherwise, it joins the fleet ahead
            # (do nothing)

        return len(stack)