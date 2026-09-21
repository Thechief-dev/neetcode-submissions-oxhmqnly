class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = [False] * n

        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        count_graph = 0

        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                count_graph += 1
        return count_graph