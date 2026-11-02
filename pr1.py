room = {
    'A': 'Dirty',
    'B': 'Dirty',
}

location = 'A'

while 'Dirty'in room.values():
    
    print("location:", location)
    print("Status:", room[location])
    
    if room[location] == 'Dirty':
        print("Action: Clean")
        room[location] = 'Clean'
        
    elif location == 'A':
        print("Action: Move Right")
        location = 'B'
        
    else:
        print("Action: Move Left")
        location = 'A'
        
    print("\nBoth rooms are cleaned!")
    print(room)
     
     