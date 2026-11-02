cities = ['A', 'B', 'C', 'D']
distance = [
    [0, 10, 20, 30],
    [10, 0, 15, 25],
    [20, 15, 0, 30],
    [30, 35, 25, 0]
]

path = [0, 1, 2, 3, 0]
cost = 0

for i in range(len(path)-1):
    cost += distance[path[i]][path[i+1]]
    
print("Best Path:", path)
print("Total distance:", cost)