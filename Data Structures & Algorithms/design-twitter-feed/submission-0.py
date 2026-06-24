import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set)  # userId -> set of followeeIds
        self.cnt = 0  # Will decrease into negative numbers to simulate Max-Heap

    def postTweet(self, userId: int, tweetId: int) -> None:
        # FIX 1 & 2: Append to the list, and make cnt negative so min-heap acts like max-heap
        self.cnt -= 1
        self.tweetMap[userId].append([self.cnt, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []
        
        # Ensure user follows themselves to see their own tweets
        self.followMap[userId].add(userId)
        
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # FIX 3: Get index based on tweetMap list length, not followMap
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                # Match strict pushing order: [count, tweetId, followeeId, next_index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        # FIX 4: Cleaned up while loop logic
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            # If this user has older tweets left, grab the next one and push it to the heap
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)   

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Protect against removing yourself or trying to unfollow someone you don't follow
        if followeeId in self.followMap[followerId] and followerId != followeeId:
            self.followMap[followerId].remove(followeeId)