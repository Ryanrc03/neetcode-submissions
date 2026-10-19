from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set) # userId ->followeeIds
        self.tweetMap = defaultdict(list) # userId -> [[count, tweetId]...]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        
    def getNewsFeed(self, userId: int) -> list[int]:
        # minHeap
        minHeap = []
        res = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index] 
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while len(res) < 10 and minHeap:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index > 0:
                count, tweetId = self.tweetMap[followeeId][index] 
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)