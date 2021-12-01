a = [int(x) for x in code.split('\n')]
last, inc = a[0]+a[1]+a[2], 0
for i in range(3,len(a)):
    c = last + a[i] - a[i-3]
    inc = inc+1 if c>last else inc
    last = c







