from functools import lru_cache

lines = open('advent-10new.raw', 'r').readlines()
m = [int(line) for line in lines]
m.append(0)
m.sort()


one = 0
three = 0
for i in range(1, len(m)):
    if m[i] - m[i-1] == 1:
        one += 1
    elif m[i] - m[i-1] == 3:
        three += 1
    else:
        print("FAIL")
three += 1

print(one, three, one*three)


@lru_cache(None)
def comb(n):
    if n == len(m)-1:
        return (1)
    ret = 0
    for i in range(3, 0, -1):
        if n+i < len(m) and m[n+i] <= m[n] + 3:
            ret += comb(n+i)
    return (ret)


print(comb(0))
