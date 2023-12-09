from pprint import pprint

f = open("16.in", "r")
lines = f.read().splitlines()
i=0
limits=dict()
while lines[i]!='':
  key, str_values = lines[i].split(': ')
  list_str_values=str_values.split(' or ')
  values = [tuple(map(int,lsv.split('-'))) for lsv in list_str_values]
  limits[key] = values
  i+=1
pprint(limits)

i+=1
assert(lines[i]=="your ticket:")
i+=1
ticket = list(map(int,lines[i].split(',')))
pprint(ticket)
i+=1
i+=1
assert(lines[i]=="nearby tickets:")
i+=1
nearby_tickets=[]
while i<len(lines):
  nearby_tickets.append(list(map(int,lines[i].split(','))))
  i+=1
  print(nearby_tickets[-1])

excluded = set(range(0,1000))
ds = dict()
for field, limit in limits.items():
    ds[field] = set(range(0,limit[0][0],))
    ds[field].update(range(limit[0][1]+1, limit[1][0],))
    ds[field].update(range(limit[1][1]+1, 1000))
    excluded.intersection_update(ds[field])
print(excluded)

pf = set(limits.keys())
possible_fields=[set(limits.keys()) for _ in range(len(ticket))]
a = 0
for nt in nearby_tickets:
    discard = False
    for v in nt:
        if v in excluded:
            a += v
            discard = True
    if not discard: #analyze
        for i, v in enumerate(nt):
            for field, excludedrange in ds.items():
                if v in excludedrange:
                    possible_fields[i].discard(field)

print(a)

print(possible_fields)
changes = True
while changes:
    changes = False
    for field in limits.keys():
        valid_in = set()
        for pos, valid_fields in enumerate(possible_fields):
            if field in valid_fields:
                valid_in.add(pos)
        if len(valid_in) == 1:
            pos = valid_in.pop()
            if len(possible_fields[pos]) != 1:
                changes = True
                possible_fields[pos] = set([field])

possible_fields = [s.pop() for s in possible_fields]
print(possible_fields)

b = 1
count = 0
for pos, field in enumerate(possible_fields):
    if field[0:len('departure')] == 'departure':
        b *= ticket[pos]
        count += 1
assert count==6
print(b)

