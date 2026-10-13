class Solution:
    def calcEquation(self, equations, values, queries):

        # Build graph
        graph = {}

        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            value = values[i]

            if a not in graph:
                graph[a] = {}

            if b not in graph:
                graph[b] = {}

            graph[a][b] = value
            graph[b][a] = 1 / value

        # DFS
        def dfs(current, target, product, visited):

            if current == target:
                return product

            visited.add(current)

            for neighbor in graph[current]:

                if neighbor not in visited:

                    result = dfs(
                        neighbor,
                        target,
                        product * graph[current][neighbor],
                        visited
                    )

                    if result != -1.0:
                        return result

            return -1.0

        # Answer queries
        answer = []

        for numerator, denominator in queries:

            # Variable doesn't exist
            if numerator not in graph or denominator not in graph:
                answer.append(-1.0)

            # Same variable
            elif numerator == denominator:
                answer.append(1.0)

            else:
                answer.append(
                    dfs(numerator, denominator, 1.0, set())
                )

        return answer