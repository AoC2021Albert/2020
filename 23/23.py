#!/usr/bin/env python

from sys import stdin
from collections import defaultdict

c = [3,6,8,1,9,5,7,4,2]
#c = [3,8,9,1,2,5,4,6,7]
rounds = 100
max = 9

# for part 2
c = [x for x in range(1,51)]
rounds=5
max=50

for round in range(rounds):
  current = c[0]
  out = c[1:4]
  remain = c[4:]
  out_set = set(out)
  found = False
  candidate = current - 1
  while not found:
    if candidate == 0:
      candidate = max
    if candidate not in out_set:
      found = True
    else:
      candidate -= 1
  candidate_pos = remain.index(candidate)
  c = remain[:candidate_pos+1] + out + remain[candidate_pos+1:] + [current]
  print(c)
  print(round)

print(c)
