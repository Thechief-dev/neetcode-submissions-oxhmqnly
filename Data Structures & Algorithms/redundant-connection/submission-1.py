class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        

        adj = [[] for _ in range(len(edges)+1)]

        for nei, edge in edges:
            adj[nei].append(edge)
            adj[edge].append(nei)
        


        visit = [False] * (len(edges) + 1)

        cycle = set()
        cycleStart = -1

        def dfs(node, parent):
            nonlocal cycleStart
            if visit[node]:
                cycleStart = node
                return True
            visit[node] = True

            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False
        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]