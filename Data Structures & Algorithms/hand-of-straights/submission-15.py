class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count ={}
        for num in hand:
            count[num] = 1 + count.get(num, 0)
        
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            starting = minHeap[0]

            for i in range(starting, starting + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True