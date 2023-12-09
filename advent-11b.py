f = open("in-11.raw", "r")
old = f.read().splitlines()

from pprint import pprint

leny = len(old)
lenx = len(old[0])

def neigh(y,x,old):
    ns = ((-1,-1), (-1, 0), (-1, 1),
          ( 0,-1),          ( 0, 1),
          ( 1,-1), ( 1, 0), ( 1, 1))
    ret = 0
    for n in ns:
        empty = True
        i = 1
        while empty:
            nx = x + n[1] * i
            ny = y + n[0] * i
            if (0 <= nx) and (nx < lenx) and (0 <= ny) and (ny < leny):
                if (old[ny][nx] != '.'):
                    empty = False
                if (old[ny][nx] == '#'):
                    ret += 1
            else:
                empty = False
            i+=1
#a        if (0 <= nx) and (nx < lenx) and (0 <= ny) and (ny < leny) and (old[ny][nx] == '#'):
#a            ret += 1
    return(ret)

flips = 1
while flips > 0:
    flips = 0
    nw = [[' '] * lenx for _ in range(leny)]
    for y in range(leny):
        for x in range(lenx):
            if old[y][x] == '.':
                nw[y][x] = '.'
            elif old[y][x] == 'L':
                if neigh(y,x,old) == 0:
                    nw[y][x] = '#'
                    flips += 1
                else:
                    nw[y][x] = 'L'
            elif old[y][x] == '#':
                if neigh(y,x,old) >= 5: #a 4:
                    nw[y][x] = 'L'
                    flips += 1
                else:
                    nw[y][x] = '#'
            else:
                assert False, "FAIL"
    print(flips, flush = True)
    old = nw
    #pprint(old)
#print(old)
print(sum(row.count('#') for row in old))

