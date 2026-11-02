
# BFS - Robot Path Planning

from collections import deque

# Grid representation
# 0 = Free cell, 1 = Obstacle

grid = [
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 0, 0]
]

# Starting and ending positions
start = (0, 0)
goal = (3, 3)

# Create a queue
queue = deque([start])

# Store visited positions
visited = {start}

# Store previous positions
parent = {start: None}

# Possible movements
directions = [
    (0, 1),   # Right
    (1, 0),   # Down
    (0, -1),  # Left
    (-1, 0)   # Up
]

# BFS traversal
while queue:

    # Remove first position
    x, y = queue.popleft()

    # Check goal
    if (x, y) == goal:
        break

    # Explore neighboring cells
    for dx, dy in directions:

        nx = x + dx
        ny = y + dy

        # Check grid boundaries
        if 0 <= nx < 4 and 0 <= ny < 4:

            # Check obstacle and visited position
            if grid[nx][ny] == 0 and (nx, ny) not in visited:

                visited.add((nx, ny))

                # Store previous position
                parent[(nx, ny)] = (x, y)

                queue.append((nx, ny))

# Display shortest path
if goal in parent:

    path = []
    current = goal

    # Trace path using parent dictionary
    while current is not None:

        path.append(current)
        current = parent[current]

    # Reverse path
    path.reverse()

    print("Robot Path:")
    print(path)

    print("Total Steps:", len(path) - 1)

else:
    print("No path found.")
