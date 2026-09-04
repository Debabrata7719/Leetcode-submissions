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

        dummy=ListNode(0)
        carry=0
        current=dummy

        while l1 is not None or l2 is not None:
            sum1= carry
            if l1 is not None:
                sum1=sum1+l1.val
            if l2 is not None:
                sum1=sum1+l2.val
            
            newNode=ListNode(sum1 % 10)
            carry = sum1 //10

            current.next=newNode
            current=current.next
            
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next

            if carry:
                current.next = ListNode(carry)

        return dummy.next




            

        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna