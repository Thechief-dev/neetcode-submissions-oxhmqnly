class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for source, target, cost in times:
            edges[source].append((target, cost))
        
        minHeap = [(0, k)] # range of cost, k starting point
        visit =  set()
        costs = 0

        while minHeap:
            cost1, target1 = heapq.heappop(minHeap)
            if target1 in visit:
                continue
            visit.add(target1)
            costs = cost1

            for target2, cost2 in edges[target1]:
                if target2 not in visit:
                    heapq.heappush(minHeap, (cost1 + cost2, target2))
        return costs if len(visit) == n else -1

