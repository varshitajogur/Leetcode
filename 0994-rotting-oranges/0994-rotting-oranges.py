from collections import deque

class Solution:
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])

        queue = deque()
        fresh = 0

        # Add all rotten oranges to the queue
        # Count fresh oranges
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue and fresh > 0:

            # Process all oranges rotten at this minute
            for _ in range(len(queue)):

                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh -= 1
                            queue.append((nr, nc))

            minutes += 1

        if fresh == 0:
            return minutes
        else:
            return -1