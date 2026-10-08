class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        frequencies = Counter(hand)

        minH = list(frequencies.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in frequencies:
                    return False
                frequencies[i] -= 1          
                if frequencies[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
