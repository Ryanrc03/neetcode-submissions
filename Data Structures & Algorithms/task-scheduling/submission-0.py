from collections import Counter,deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # cnt: next time
        while maxHeap or q:
            time += 1

            # not item in heap but need to idle
            if not maxHeap:
                time = q[0][1] # start from next 
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: # need to process again
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time