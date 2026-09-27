from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq =[[] for i in range(len(nums) + 1)] # bucket

        for num in nums:
            count[num] += 1

        for num, c in count.items():
            freq[c].append(num)

        # get result
        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
            if len(res) == k:
                return res