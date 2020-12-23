def get_element(formula,pos, func):
    if formula[pos] == "(":
        pos += 1
        val, pos = func(formula,pos)
        assert(formula[pos] == ")")
        pos += 1
    else:
        val = 0
        while pos<len(formula) and formula[pos] in [str(i) for i in range(10)]:
            val *= 10
            val += int(formula[pos])
            pos +=1
    return(val, pos)


def analyze(formula, pos):
    val, pos=get_element(formula,pos,analyze)
    while pos < len(formula) and formula[pos] in ['*','+']:
        op = formula[pos]
        val2, pos = get_element(formula,pos+1,analyze)
        if op == "+":
            val += val2
        else:
            assert op == "*"
            val *= val2
    return(val,pos)

def analyzeb(formula, pos):
    val, pos = get_element(formula,pos, analyzeb)
    while pos < len(formula) and formula[pos] in ['*','+']:
        op = formula[pos]
        if op == "*":
            val2, pos = analyzeb(formula, pos+1)
        else:
            val2, pos = get_element(formula,pos+1,analyzeb)
        if op == "+":
            val += val2
        else:
            assert op == "*"
            val *= val2
    return(val,pos)


lines = open("advent-18.raw").readlines()
a = 0
b = 0
for formula in lines:
    formula = formula.replace(" ","")
    formula = formula.replace("\n","")

    vala, pos = analyze(formula, 0)
    assert pos == len(formula)
    a += vala

    valb, pos = analyzeb(formula, 0)
    assert pos == len(formula)
    b += valb

    print(formula, vala, valb)

print(a,b)
