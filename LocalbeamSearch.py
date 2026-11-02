
# Local Beam Search - Traveling Salesman Problem

# Distance between 4 cities
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Calculate total route distance
def calculate_cost(route):

    cost = 0

    for i in range(len(route) - 1):
        cost += distance[route[i]][route[i + 1]]

    # Return to starting city
    cost += distance[route[-1]][route[0]]

    return cost


# Generate neighboring routes
def get_neighbors(route):

    neighbors = []

    for i in range(1, len(route)):

        for j in range(i + 1, len(route)):

            new_route = route.copy()

            # Swap two cities
            new_route[i], new_route[j] = new_route[j], new_route[i]

            neighbors.append(new_route)

    return neighbors


# Local Beam Search
def beam_search():

    K = 3  # Number of routes to keep

    # Initial routes
    beam = [
        [0, 1, 2, 3],
        [0, 2, 1, 3],
        [0, 3, 2, 1]
    ]

    best_route = None
    best_cost = float('inf')

    # Repeat search
    for iteration in range(20):

        candidates = []

        # Generate neighboring routes
        for route in beam:

            candidates.append(route)
            candidates.extend(get_neighbors(route))

        # Sort routes by distance
        candidates.sort(key=calculate_cost)

        # Keep best K routes
        beam = candidates[:K]

        # Update best route
        current_cost = calculate_cost(beam[0])

        if current_cost < best_cost:

            best_cost = current_cost
            best_route = beam[0].copy()

    return best_route, best_cost


# Main program
route, cost = beam_search()

print("Best Route:")

for city in route:
    print(city, end=" -> ")

print(route[0])

print("Minimum Distance:", cost)
