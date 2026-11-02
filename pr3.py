start = [1,2,3,4,0,6,7,5,8]
goal = [1,2,3,4,5,6,7,8,0]

def h(s):
    return sum(s[i]!= goal[i] and s[i]!= 0 for i in range(9))

open_list = [(start, 0)]
visited = []

while open_list:
    open_list.sort(key = lambda x: x[1] + h(x[0]))
    s, cost = open_list.pop(0)
    
    if s == goal:
        print("Goal Reached!")
        print(s)
        break
    
    if s not in visited:
        visited.append(s)
        z = s.index(0)
        
        for m in [z-3, z+3, z-1, z+1]:
            if 0 <= m < 9 and not (z % 3 == 0 and m == z-1) and not (z % 3 == 2 and m == z+1):
                n = s.copy()
                n[z], n[m] = n[m], n[z]
                
                if n not in visited:
                    open_list.append((n, cost + 1))

