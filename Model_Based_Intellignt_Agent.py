
# Model-Based Agent - Grid Navigation

from collections import deque

# Grid: 0 = Free cell, 1 = Obstacle
grid = [
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 0, 0]
]

# Starting and goal positions
start = (0, 0)
goal = (3, 3)

# Queue for BFS
queue = deque([start])

# Remember visited positions
visited = {start}

# Possible movements
directions = [
    (0, 1),   # Right
    (1, 0),   # Down
    (0, -1),  # Left
    (-1, 0)   # Up
]

print("Agent started at:", start)

while queue:

    # Remove first position from queue
    x, y = queue.popleft()

    print("Agent position:", (x, y))

    # Check whether goal is reached
    if (x, y) == goal:
        print("Goal Reached!")
        break

    # Explore neighboring cells
    for dx, dy in directions:

        nx = x + dx
        ny = y + dy

        # Check grid boundaries
        if 0 <= nx < 4 and 0 <= ny < 4:

            # Avoid obstacles and visited cells
            if grid[nx][ny] == 0 and (nx, ny) not in visited:

                visited.add((nx, ny))
                queue.append((nx, ny))

else:
    print("Goal cannot be reached.")
