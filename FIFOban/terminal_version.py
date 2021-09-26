# sokoban in terminal with list

pl_pos = [3, 2]
box_place = [2, 2]
g = 0
p = 7
w = 4
b = 2
c = 9
level = [
    [w,w,w,w,w,w],
    [w,g,g,g,g,w],
    [w,g,c,b,g,w],
    [w,g,p,g,g,w],
    [w,g,g,g,g,w],
    [w,w,w,w,w,w]
]


def print_level(level):
    for i in range(len(level)):
        print(level[i])

def move_player(x, y, box_pos=[0, 0], box=False):
    global pl_pos
    global box_place

    if box:
        level[pl_pos[0]+box_pos[1]][pl_pos[1]+box_pos[0]] = b

    level[pl_pos[0]][pl_pos[1]] = g
    level[pl_pos[0]+y][pl_pos[1]+x] = p
    pl_pos = [pl_pos[0]+y, pl_pos[1]+x]

    if (level[box_place[0]][box_place[1]] == b) or (level[box_place[0]][box_place[1]] == p):
        pass
    else:
        level[box_place[0]][box_place[1]] = c

def get_obj(x, y):
    obj = level[pl_pos[0]+y][pl_pos[1]+x]
    return obj

def move(dr):
    if dr == "a":
        obj = get_obj(-1, 0)
        if obj == g:
            move_player(-1, 0)
        elif obj == b:
            if get_obj(-2, 0) == g or get_obj(-2, 0) == c:
                move_player(-1, 0, box=True, box_pos=[-2, 0])

    elif dr == "d":
        obj = get_obj(1, 0)
        if obj == g:
            move_player(1, 0)
        elif obj == b:
            if get_obj(2, 0) == g or get_obj(2, 0) == c:
                move_player(1, 0, box=True, box_pos=[2, 0])

    elif dr == "s":
        obj = get_obj(0, 1)
        if obj == g:
            move_player(0, 1)
        elif obj == b:
            if get_obj(0, 2) == g or get_obj(0, 2) == c:
                move_player(0, 1, box=True, box_pos=[0, 2])

    elif dr == "w":
        obj = get_obj(0, -1)
        if obj == g:
            move_player(0, -1)
        elif obj == b:
            if get_obj(0, -2) == g or get_obj(0, -2) == c:
                move_player(0, -1, box=True, box_pos=[0, -2])


while True:
    print_level(level=level)
    inp = str(input(">>"))
    move(inp)
    if inp == "q":
        break