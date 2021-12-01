a = []
word = ""
for i in range(len(code)):
    l = code[i]
    if l.isnumeric():
        word+=l
    else:
        a.append(int(word))
        word = ""

inc = 0
d = 0
last = a[0]+a[1]+a[2]
for i in range(3,len(a)):
    c = last + a[i] - a[i-3]
    if(c>last):
        inc+=1
    last = c
print(a)
print(inc)







