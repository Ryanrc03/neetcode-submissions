from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # data stru: adj list, min heap -> path sum, node
        # bfs 
        edges = defaultdict(list)
        for u, v, w in edges:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        time = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            time = w1

            for w2, n2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return time if len(visit) == n else -1