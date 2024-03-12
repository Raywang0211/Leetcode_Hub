# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(1)
        dummy_head.next = head
        
        pre = dummy_head
        cur = dummy_head.next

        while cur:
            if cur.val==val:
                pre.next = cur.next
            else:
                pre = cur
            
            cur = cur.next
        
        return dummy_head.next

