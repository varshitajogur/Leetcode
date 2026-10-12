class Solution:
    def minReorder(self, n, connections):
        graph = [[] for _ in range(n)]

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = [False] * n

        def dfs(city):
            visited[city] = True
            changes = 0

            for next_city, cost in graph[city]:
                if not visited[next_city]:
                    changes += cost
                    changes += dfs(next_city)

            return changes

        return dfs(0)