def a(m,limit):
    turn=len(m)
    last_spoken = m[-1]

    while turn < 2020:
        turn += 1
        try:
            distance = list(reversed(m[:-1])).index(last_spoken)+1
        except ValueError:
            distance = 0
        m.append(distance)
        last_spoken = distance
    return(m[-1])

def ab(m, limit):
    d = dict()
    for i, v in enumerate(m[:-1]):
        d[v] = i + 1
    turn=len(m)
    last_spoken = m[-1]

    while turn < limit:
        if last_spoken in d:
            distance = turn - d[last_spoken]
        else:
            distance = 0
        d[last_spoken] = turn
        turn += 1
        last_spoken = distance
    return(distance)



for limit in [2020, 30000000]:
    print(ab([17,1,3,16,19,0],limit))
    print(ab([0,3,6],limit))
    print(ab([1,3,2],limit))
    print(ab([2,1,3],limit))
    print(ab([1,2,3],limit))
    print(ab([2,3,1],limit))
    print(ab([3,1,2],limit))
    print()



