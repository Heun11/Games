import os

pl_pos = [0, 0]

g = 0
p = 1
w = 2
r = 3

level = [
    [p,g,g,g,g,g],
    [r,g,g,g,g,g],
    [r,r,r,r,w,g],
    [g,g,r,r,w,g],
    [g,g,r,r,w,g],
    [g,g,g,g,g,g]
]

def print_level(level):
    print()
    for i in range(len(level)):
        for j in range(len(level[i])):
            print(f"{level[i][j]} ", end="")
        print()

def get_obj(x, y):
    obj = level[pl_pos[0]+y][pl_pos[1]+x]
    return obj

def move_player(x, y):
    global pl_pos, level
    level[pl_pos[0]][pl_pos[1]] = r
    level[pl_pos[0]+y][pl_pos[1]+x] = p
    pl_pos = [pl_pos[0]+y, pl_pos[1]+x]

def move(x, y):
    obj = get_obj(x, y)
    if obj == r:
        move_player(x, y)

while True:
    print_level(level)
    d = input(">> ")
    if d=="a":
        move(-1,0)

    elif d=="d":
        move(1,0)

    elif d=="w":
        move(0,-1)
    
    elif d=="s":
        move(0,1)

    else:
        print("WRONG KEY, USE a,w,s,d TO MOVE")
