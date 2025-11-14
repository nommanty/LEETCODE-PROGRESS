# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # A link list is a list wich has to be entered by its head wich is the first item of it:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

    # We define two pointers:
        slow = head
        fast = head

    #  We use a while loop to evaluate when the fast pointer is about to surpass the last linked item
    # And we choose to evaluate also "fast" because if "fast" is already none, the first part of the conditional is "false" so the other part doesn't evaluate,
    # Wich is good beacuse in that case "fast.next" would be an error, because you can't not evaluate "next" on a "none"
        while fast and fast.next:

        # Our pointers will run trough the items, one step by step and the other one two steps by two steps
            slow = slow.next
            fast = fast.next.next

    # When the loop breaks it means our "fast" pointer is directing to the last item or has surpased by one and is a "none" value

        return slow 







