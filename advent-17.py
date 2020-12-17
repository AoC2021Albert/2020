from copy import deepcopy
m=[
'..##.#.#',
'.#####..',
'#.....##',
'##.##.#.',
'..#...#.',
'.#..##..',
'.#...#.#',
'#..##.##']

space=[[[[0] * 24 for _ in range(24)] for _ in range(24)] for _ in range(24)]

for rowi, row in enumerate(m):
    for coli, p in enumerate(row):
        space[8][8][8+rowi][8+coli] = 0 if p=='.' else 1

for turns in range(6):
    nspace = deepcopy(space)
    for x in range(1,23):
        for y in range(1,23):
            for z in range(1,23):
                for w in range(1,23):
                    an = 0
                    for xd in [-1,0,1]:
                        for yd in [-1,0,1]:
                            for zd in [-1,0,1]:
                                for wd in [-1,0,1]:
                                    if space[x+xd][y+yd][z+zd][w+wd] == 1:
                                        an +=1
                    if space[x][y][z][w] == 1:
                        if an-1 != 2 and an-1!=3:
                            nspace[x][y][z][w] = 0
                    else:
                        if an == 3:
                            nspace[x][y][z][w] = 1
    space = nspace

active=0
for x in range(1,23):
    for y in range(1,23):
        for z in range(1,23):
            for w in range(1,23):
                if space[x][y][z][w] == 1:
                    active+=1
print(active)





