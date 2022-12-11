#!/usr/bin/env python

from sys import stdin
from collections import defaultdict

# grep [0-9] in.raw | sed 's/Player /p/ ; s/$/,/ ; s/:,/=\[/' >> 22.py
p1=[
9,
2,
6,
3,
1]
p2=[
5,
8,
4,
7,
10]

p1=[
50,
14,
10,
17,
38,
40,
3,
46,
39,
25,
18,
2,
41,
45,
7,
47,
36,
1,
30,
32,
8,
31,
12,
5,
28]
p2=[
9,
6,
37,
42,
22,
4,
21,
15,
44,
16,
29,
43,
19,
11,
13,
24,
48,
35,
26,
23,
27,
33,
20,
49,
34]

while len(p1) and len(p2):
  if p1[0] < p2[0]:
    p1,p2=p2,p1
  p1=p1[1:]+[p1[0]]+[p2[0]]
  p2=p2[1:]

r=0
lp1=len(p1)
for i in range(lp1):
  r += (lp1-i) * p1[i]

print(r)


## PART 2

p1=[
50,
14,
10,
17,
38,
40,
3,
46,
39,
25,
18,
2,
41,
45,
7,
47,
36,
1,
30,
32,
8,
31,
12,
5,
28]
p2=[
9,
6,
37,
42,
22,
4,
21,
15,
44,
16,
29,
43,
19,
11,
13,
24,
48,
35,
26,
23,
27,
33,
20,
49,
34]


def game(p):
  seen0=[p[0]]
  while len(p[0]) and len(p[1]):
    if (p[0][0]<len(p[0])) and (p[1][0]<len(p[1])):
      winner, ignore = game([p[0][1:p[0][0]+1], p[1][1:p[1][0]+1]])
    else:
      winner=0 if (p[0][0]>p[1][0]) else 1
    loser = (winner + 1 ) % 2
    p[winner], p[loser] = p[winner][1:] + [p[winner][0]] + [p[loser][0]], p[loser][1:]
    for i in range(len(seen0)):
      if seen0[i]==p[0]:
        p[1]=[]
        winner=0
    seen0.append(p[0])
  return (winner, p[winner])

ignore, p = game([p1,p2])
r=0
lp=len(p)
for i in range(lp):
  r += (lp-i) * p[i]

print(r)
