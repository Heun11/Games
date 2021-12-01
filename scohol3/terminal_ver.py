f_0 = [
    [1,0,0,0,0],
    [1,0,0,1,0],
    [1,1,0,1,0],
    [0,1,1,1,0],
    [0,1,0,0,0]
]

f_1 = [
    ["P",0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,"M1",0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

pl_pos = [0,0]
m = [[2, 3]]

def print_level(f_0, f_1):
    print()
    for i in range(len(f_0)):
        for j in range(len(f_0[i])):
            print(f"{f_0[i][j]}", end=" ")

        print(f"|", end=" ")

        for k in range(len(f_1[i])):
            print(f"{f_1[i][k]}", end=" ")

        print()

def get_obj(x, y):
    return f_1[y][x]

def move_player(x, y):
    pass

def move_enemies():
    pass

def move(x, y):
    move_enemies()

while True:
    print_level(f_0,f_1)
    d = input(">> ")
    if d=="a":
        move(-1,0)

    elif d=="d":
        move(1,0)

    elif d=="w":
        move(0,-1)
    
    elif d=="s":
        move(0,1)