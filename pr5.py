from collections import deque

start = ('A', 'B', 'C')
goal = ('C', 'B', 'A')

queue = deque([start])
visited = [start]

while queue:
    state = queue.popleft()
    
    if state == goal:
        print("Goal Reached!")
        print(state)
        break
    
    new_state = state[::-1]
    
    if new_state not in visited:
        visited.append(new_state)
        queue.append(new_state)