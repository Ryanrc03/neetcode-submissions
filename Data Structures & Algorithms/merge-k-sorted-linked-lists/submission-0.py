
import heapq
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        minHeap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, [node.val, i, node])

        dummy = ListNode(0)
        cur = dummy

        while minHeap:
            val, i, node = heapq.heappop(minHeap)

            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(minHeap, [node.next.val, i, node.next])
        return dummy.next