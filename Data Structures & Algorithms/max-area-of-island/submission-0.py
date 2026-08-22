class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [
            (-1, 0),   # up
            (1, 0),    # down
            (0, -1),   # left
            (0, 1)     # right
        ]

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                # Found a new island
                if grid[r][c] == 1:

                    q = deque()
                    q.append((r, c))

                    # Mark visited
                    grid[r][c] = 0

                    area = 0

                    while q:

                        row, col = q.popleft()

                        area += 1

                        # Check 4 directions
                        for dr, dc in directions:

                            nr = row + dr
                            nc = col + dc

                            # Check if valid land
                            if (0 <= nr < rows and
                                0 <= nc < cols and
                                grid[nr][nc] == 1):

                                grid[nr][nc] = 0
                                q.append((nr, nc))

                    max_area = max(max_area, area)

        return max_area


        