# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None: 
            return None
        node_before_target = head
        cur = head
        for i in range(n): 
            cur = cur.next
        # when n = len(linked list)
        if not cur: 
            return head.next
        while cur.next: 
            cur = cur.next
            node_before_target = node_before_target.next
        temp = node_before_target.next.next;
        node_before_target.next = temp
        return head
        
            
        