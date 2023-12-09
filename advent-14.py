f = open("14.in", "r")
lines = f.read().splitlines()
m=[]
for line in lines:
  left, right = line.split(' = ')
  if left != "mask":
    left = int(left[4:-1])
    right = int(right)
  m.append((left,right))

mem = dict()
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
for p in m:
    if p[0] == "mask":
        mask = p[1]
        mask0 =  2 ** len(mask) - 1
        mask1 = 0
        for i,c in enumerate(mask):
            if c == "0":
                mask0 = mask0 & ~(1 << (len(mask) - 1 - i))
            if c == "1":
                mask1 = mask1 | (1 << (len(mask) - 1 - i))
    else:
        mem[p[0]] = (p[1] & mask0) | mask1
print("a", sum(v for v in mem.values()))
#b
mem = dict()
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
for p in m:
    if p[0] == "mask":
        mask = p[1]
        mask0 =  2 ** len(mask) - 1
        mask1 = 0
        maskx = []
        for i,c in enumerate(mask):
            if c == "1":
                mask1 = mask1 | (1 << (len(mask) - 1 - i))
            if c == "X":
                mask0 = mask0 & ~(1 << (len(mask) - 1 - i))
                maskx.append(i)
    else:
        if maskx:
            baseaddr = (p[0] & mask0) | mask1
            for bits in range(2**len(maskx)):
                addr = baseaddr
                # We bet a list with the bits of `bits`. Probably can be done nicer.
                bitslist = [int(b) for b in list(format(bits, '0'+str(len(maskx))+'b'))]
                for bitpos in range(len(maskx)):
                    addr = addr | (bitslist[bitpos] << (len(mask) - 1 - maskx[bitpos]))
                mem[addr] = p[1]
#                print(f"p[0]: {p[0]}, maskx: {maskx}, bitslist: {bitslist}, mask: \n{mask}, baseaddr: \n{format(baseaddr,'036b')}, addr: \n{format(addr,'036b')}")
        else:
            mem[p[0] | mask1] = p[1]
print("b", sum(v for v in mem.values()))
