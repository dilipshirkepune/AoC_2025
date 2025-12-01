# for left operations
arr = list(range(0, 100))
length = len(arr)
count = 0
start = arr.index(50)
rotations = []

part = 2  # Change to 1 for part 1

with open("input.txt") as f:
    rotations = [r.strip() for r in f.read().split('\n')]


for i in rotations:
    times = 0
    if i[0] == 'L':
        travel_distance = int(i[1:])        
        times = travel_distance // 100
        travel_distance %= 100
        distance = arr.index(start)
        if(travel_distance > distance):
            start =  arr[length-abs(travel_distance-arr.index(start))]
            if(distance != 0 and part == 2):     
                count += 1                       
        else:
            start = arr[arr.index(start)-travel_distance]            
    else:
        right = int(i[1:])        
        times = right // 100
        right %= 100
        distance = arr.index(start)
        if(length <= distance+right):
            start =  arr[abs(length - (distance+right))]      
            if(length != distance+right and part == 2):
                count += 1                     
        else:
            start = arr[arr.index(start)+right]            
    
    if(start == 0):
        count += 1        
    if(times != 0 and part == 2):
        count += times
    

print(count)
