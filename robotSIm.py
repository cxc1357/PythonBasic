#day61:模拟机器人行走

def robotSim(commands,obstacles):
    obstacles = set(map(tuple,obstacles))
    d = 0
    vectors = [[0,1],[-1,0],[0,-1],[1,0]]
    x,y,maxd = 0,0,0
    for command in commands:
        if command == -2:
            d = (d + 1) % 4
        elif command == -1:
            d = (d - 1) % 4
        else:
            vector = vectors[d]
            while command > 0:
                if( x + vector[0],y+vector[1]) not in obstacles:
                    x,y = x + vector[0],y + vector[1]
                command -= 1
            maxd = max(maxd, x**2+y**2)
        return maxd

        