# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        
        previous = dummy
        current = head
        
        while current:
            
            # Duplicate found
            if current.next and current.val == current.next.val:
                
                duplicate = current.val
                
                # Skip all nodes with this value
                while current and current.val == duplicate:
                    current = current.next
                
                previous.next = current
            
            else:
                previous = current
                current = current.next
        
        return dummy.next

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna