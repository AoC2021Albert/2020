#!/usr/bin/env python

from sys import stdin
from collections import defaultdict

#c = [3,8,9,1,2,5,4,6,7]
c = [3,6,8,1,9,5,7,4,2]
rounds=10000000
elements=1000000

#The value on cups[i] will be which is the element to the right of the cup with number i
next_cup=[i+1 for i in range(elements)]
next_cup.append(c[0])
#we will ingore position 0

for i in range(len(c)-1):
   next_cup[c[i]] = c[(i+1) % 9]
next_cup[c[-1]]=len(c)+1

#print(next_cup)
pos = c[0]
for round in range(rounds):

  out_set = set()
  out = next_cup[pos]
  for i in range(3):
    out_set.add(out)
    out=next_cup[out]
  out_head = next_cup[pos]
  next_cup[pos] = out

  insertion_point = elements if pos == 1 else pos - 1
  while insertion_point in out_set:
    insertion_point = elements if insertion_point == 1 else insertion_point - 1
  
  insertion_end = next_cup[insertion_point]
  next_cup[insertion_point] = out_head
  for i in range(3-1):
    out_head = next_cup[out_head]
  next_cup[out_head]=insertion_end

  pos = next_cup[pos]

  #print(next_cup)

next = next_cup[1]
for i in range(2):
  print(next)
  next=next_cup[next]
