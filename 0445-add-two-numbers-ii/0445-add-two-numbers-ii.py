# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack1 = []
        stack2 = []
        
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
            
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        carry = 0
        head = None 
        while stack1 or stack2 or carry != 0:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            
            new_node = ListNode(total % 10)
            
           
            new_node.next = head
            head = new_node
            
        return head


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna