# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        refs = [] # list of ref nodes
        cur = head
        while cur != None: 
            for ref in refs: 
                if ref.next == cur: 
                    return True
            newRef = ListNode(cur.val, cur)
            refs.append(newRef)
            cur = cur.next
        return False
        
        