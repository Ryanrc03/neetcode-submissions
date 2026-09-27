class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        sp = fp = head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
            if sp == fp:
                return True
        return False