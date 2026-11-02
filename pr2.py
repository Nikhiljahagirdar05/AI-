matrix = [
    ['S', '0', 'X'],
    ['0', '0', 'X'],
    ['X', '0', 'G']
]

position = [0, 0]
memory = []

while matrix[position[0]][position[1]] != 'G':
    
    x,y = position
    memory.append([x,y])
    
    print("Current Position:", position)
    
    if y<2 and matrix[x][y+1] != 'X':
        position = [x, y+1]
        
    if x<2 and matrix[x+1][y] != 'X':
        position = [x+1, y]
        
    else:
        print("Obstacle Found!")
        break
    print("Memory:", memory)
    
    if matrix[position[0]][position[1]] == 'G':
        print("Goal Reached!")