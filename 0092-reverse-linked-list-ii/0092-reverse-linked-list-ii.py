class Solution(object):
    def reverseBetween(self, head, left, right):

        current = head
        previous = None

        i = 1

        # Move current to left
        while current is not None and i != left:
            previous = current
            current = current.next
            i += 1

        pointertostart = previous
        start = current

        previous = None

        # Reverse from left to right
        while current is not None and i <= right:
            next_node = current.next

            current.next = previous
            previous = current

            current = next_node
            i += 1

        # Connect the first part to reversed part
        if pointertostart is not None:
            pointertostart.next = previous
        else:
            head = previous

        # Connect reversed part to remaining list
        start.next = current

        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna