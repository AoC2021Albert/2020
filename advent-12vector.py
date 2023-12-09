f = open("12.in", "r")
lines = f.read().splitlines()

m = []
for line in lines:
    m.append((line[0],int(line[1:])))

nsew = {
    "N": ( 1, 0),
    "S": (-1, 0),
    "E": ( 0, 1),
    "W": ( 0,-1)
}
headings= "ESWN"
HEADINGCHUNK = 90 #degrees, granularity given

def vector_sum(a,b):
    return(list(map(sum, zip(a,b))))

def vector_mul(a,b):
    return(x * b for x in a)

headingidx = 0
pos = (0, 0)
for move in m:
    if move[0] in "LR":
        sign = 1 if move[0]=="R" else -1
        headingidx = ( headingidx + (sign * (move[1] // HEADINGCHUNK))) % len(headings)
    else:
        effective_heading = headings[headingidx] if move[0] == "F" else move[0]
        pos = vector_sum(pos, vector_mul( nsew[effective_heading], move[1]))
    print(move,pos)
print(sum(abs(x) for x in pos))

# B
pos = (0, 0)
wp = (1, 10)
trans = {
    0  : lambda v: [ v[0],  v[1]], #for completeness
    90 : lambda v: [-v[1],  v[0]],
    180: lambda v: [-v[0], -v[1]],
    270: lambda v: [ v[1], -v[0]]
}
for move in m:
    if move[0] in "LR":
        right_degrees = 360 - move[1] if move[0] == "L" else move[1]
        wp = trans[right_degrees](wp)
    elif move[0] == "F":
        pos = vector_sum(pos, vector_mul( wp, move[1]))
    else:
        wp = vector_sum(wp, vector_mul(nsew[move[0]], move[1]))
    print(move,pos, wp)
print(sum(abs(x) for x in pos))

