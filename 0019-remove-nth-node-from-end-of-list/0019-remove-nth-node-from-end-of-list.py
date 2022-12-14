# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None: 
            return None
        
        # pointer 1st move 1st
        cur = head
        for i in range(n): 
            cur = cur.next
            
        # when n = len(linked list)
        if not cur: 
            return head.next
        
        # pointer 2 moves 2nd
        node_before_target = head
        while cur.next: 
            cur = cur.next
            node_before_target = node_before_target.next
        # remove the target node
        temp = node_before_target.next.next;
        node_before_target.next = temp
        return head
        
            
        