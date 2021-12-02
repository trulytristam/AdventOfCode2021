def answer(instr):
    h,d,a = 0,0,0
    v = {"n": [1,0], "p":[-1,0], "d":[0,1]}
    for i in range(len(instr)):
        if instr[i].isnumeric():
            n = int(instr[i])
            a+=n*v[instr[i-2]][0]
            h+=n*v[instr[i-2]][1]
            d+=a*n*v[instr[i-2]][1]
    return d*h
