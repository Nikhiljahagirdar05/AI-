
# A* Search Algorithm - 8 Puzzle

import heapq

# Goal state
goal = "123456780"

# Calculate Manhattan Distance
def heuristic(state):

    distance = 0

    for i in range(9):

        tile = state[i]

        if tile != '0':

            # Current position
            current_row = i // 3
            current_col = i % 3

            # Goal position
            value = int(tile) - 1

            goal_row = value // 3
            goal_col = value % 3

            # Calculate Manhattan Distance
            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


# Generate neighboring states
def get_neighbors(state):

    neighbors = []

    zero = state.index('0')

    row = zero // 3
    col = zero % 3

    # Possible movements
    directions = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1)
    ]

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_pos = new_row * 3 + new_col

            # Swap blank space with neighboring tile
            arr = list(state)

            arr[zero], arr[new_pos] = arr[new_pos], arr[zero]

            neighbors.append("".join(arr))

    return neighbors


# A* Search
def astar(start):

    # Priority queue stores (f, g, state)
    pq = [(heuristic(start), 0, start)]

    # Store minimum cost to reach each state
    cost = {start: 0}

    # Store parent states
    parent = {start: None}

    while pq:

        f, g, current = heapq.heappop(pq)

        # Skip outdated entries
        if g != cost[current]:
            continue

        # Check goal
        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        # Explore neighboring states
        for next_state in get_neighbors(current):

            new_cost = g + 1

            if next_state not in cost or new_cost < cost[next_state]:

                cost[next_state] = new_cost
                parent[next_state] = current

                new_f = new_cost + heuristic(next_state)

                heapq.heappush(
                    pq, (new_f, new_cost, next_state)
                )

    return None


# Main program
start = input("Enter initial state (9 digits, use 0 for blank): ")

if len(start) != 9 or not start.isdigit() or set(start) != set("012345678"):
    print("Invalid input!")
else:

    solution = astar(start)

    if solution:

        print("\nGoal Reached!")
        print("Solution Steps:")

        for state in solution:

            for i in range(0, 9, 3):
                print(" ".join(state[i:i+3]))

            print()

        print("Total Moves:", len(solution) - 1)

    else:
        print("No solution found.")
