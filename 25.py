def getval(n,loops):
    r=n
    for _ in range(loops):
        r*=n
        r%=20201227
    return(r)

def findloops(a,b):
    n=7
    found=0
    loop=0
    r = {}
    while found < 2 :
        if n in [a,b]:
           found+=1
           print(f'found {n} at loop {loop}')
           r[n]=loop
        loop += 1
        n*=7
        n%=20201227
    return(r)

def solve(a,b):
    loops= findloops(a,b)
    print(f'result {getval(a,loops[b])}, {getval(b,loops[a])}')

#sample
solve(5764801, 17807724)

#problem
solve(11404017, 13768789)
