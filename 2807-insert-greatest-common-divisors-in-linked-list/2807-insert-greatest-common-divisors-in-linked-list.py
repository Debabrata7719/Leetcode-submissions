# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution(object):
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        
        if head.next is None:
            return head

        current=head

        while current and current.next:

            gcd=self.gcd(current.val,current.next.val)

            gcdnode=ListNode(gcd)

            gcdnode.next=current.next
            current.next=gcdnode
            current=gcdnode.next

        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna