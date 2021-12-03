t = ["0","1"]
def ratings(a,flip,ind=0):
    global t
    if(len(a)==1):
        return a[0]
    z = 0;
    for i in range(len(a)):
        z = z+1 if a[i][ind]==t[flip] else z
    za = z if not flip else (len(a)-z)
    zb = (len(a)-z) if not flip else z
    m = t[flip] if za > zb else t[not flip]
    newa = [];
    for i in range(len(a)): 
        if a[i][ind] == m:
            newa.append(a[i])
    return ratings(newa,flip, ind+1)
def answer(code):
    a = code.split("\n")
    return int(ratings(a,0),2) * int(ratings(a,1),2)
