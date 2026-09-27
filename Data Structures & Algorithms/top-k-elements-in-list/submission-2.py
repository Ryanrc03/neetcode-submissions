class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = list(count.items())
        arr.sort(key = lambda x: x[1], reverse= True)

        res = []
        for i in range(k):
            res.append(arr[i][0])
        return res