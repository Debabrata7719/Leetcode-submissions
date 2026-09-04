"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):

        if head is None:
            return None

        mapping = {}

        # Create copies
        pointer = head

        while pointer is not None:
            mapping[pointer] = Node(pointer.val)
            pointer = pointer.next

        # Connect next and random
        pointer = head

        while pointer is not None:
            new_pointer = mapping[pointer]

            new_pointer.next = mapping.get(pointer.next)
            new_pointer.random = mapping.get(pointer.random)

            pointer = pointer.next

        return mapping[head]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna