class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort(reverse=True)
        for src, dst in tickets:
            graph[src].append(dst)
        
        route = []
        def dfs(node):

            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)
            route.append(node)

        dfs("JFK")
        return route[::-1]

        