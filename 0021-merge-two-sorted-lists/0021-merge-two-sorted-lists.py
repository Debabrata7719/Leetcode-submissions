class Solution(object):
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode(0)
        current = dummy

        while list1 is not None and list2 is not None:

            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1 is not None:
            current.next = list1
        else:
            current.next = list2

        return dummy.next

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna