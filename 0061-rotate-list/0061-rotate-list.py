# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if head is None or head.next is None:
            return head

        length = 1
        tail=head

        while tail.next:
            tail=tail.next
            length +=1

        k=k%length

        if k==0:
            return head

        steps=length-k-1

        new_tail=head

        for _ in range(steps):
            new_tail=new_tail.next

        new_head=new_tail.next

        new_tail.next=None

        tail.next=head

        return new_head

        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna