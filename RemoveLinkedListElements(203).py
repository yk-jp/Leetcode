# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode()
        dummy.next = head
        iterator = dummy
     
        while iterator.next:
            if iterator.next.val == val:
                if not iterator.next.next:
                    iterator.next = None
                    continue
                iterator.next = iterator.next.next
                continue
            iterator = iterator.next

        return dummy.next