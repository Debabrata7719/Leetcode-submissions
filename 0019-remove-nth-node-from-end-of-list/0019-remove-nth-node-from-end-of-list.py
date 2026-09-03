# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        slow=dummy
        fast=dummy

        for i in range(n):
            fast=fast.next

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next

            
        slow.next=slow.next.next

        return dummy.next


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna