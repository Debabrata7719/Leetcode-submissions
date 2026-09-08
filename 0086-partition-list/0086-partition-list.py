# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        current=head

        dummyBig=ListNode(0)

        dummySmall=ListNode(0)

        smalltail=dummySmall
        bigtail=dummyBig

        while current is not None :
            if current.val < x:
                smalltail.next = current 
                smalltail= smalltail.next
            else:
                bigtail.next = current
                bigtail=bigtail.next

            current=current.next

        smalltail.next=dummyBig.next

        bigtail.next = None

        return dummySmall.next


            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna