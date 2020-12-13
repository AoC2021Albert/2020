t=1005526
m=[37,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,41,0,0,0,0,0,0,0,0,0,587,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,19,0,0,0,23,0,0,0,0,0,29,0,733,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,17]

minwait = t
minid = 0
for id in m:
    if id and id - (t % id) < minwait:
        minwait = id - (t % id)
        minid = id
print(minid, minwait, minwait*minid)

#B
mul = 1
offset = 0
for i, id in enumerate(m):
    if id:
        j = 0
        # note: For this to work all id pairs have to be coprimes.
        # I have verified all id's given in the list are prime (and hence coprimes)
        # If they were NOT coprimes, we should check if there was no possible solution.
        # That would be easy. After `j+=1` we would check if j > id. In that case we would have found an unsolvable configuration.
        while ((j * mul + offset) % id) != (id - (i % id)) % id:
            j += 1
        offset = (j * mul + offset)
        mul *= id
print(offset)
