class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals:
            lastEnd = res[-1][1]

            if start <= lastEnd: # merge
                res[-1][1] = max(lastEnd, end)
            else: # not merge
                res.append([start, end])
        return res
