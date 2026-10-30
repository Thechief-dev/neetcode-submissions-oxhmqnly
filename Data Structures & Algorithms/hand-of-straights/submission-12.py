class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        freq = {}
        for num in hand:
            freq[num] = 1 + freq.get(num, 0)
        
        minHeap = list(freq.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]
            
            for i in range(first, first + groupSize):
                if i not in freq:
                    return False
                freq[i] -= 1

                if freq[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True