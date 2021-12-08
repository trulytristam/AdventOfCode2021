def av(n):
    return sum(n)//len(n)
def cost(n):
    return (n*(n+1))/2
def fuel(n,i):
    return sum(list(map(lambda x: cost(abs(i-x)), n)))
def answer(code):
    code = list(map(int,code.replace(",","*").split("*")))
    average = av(code)
    gradient = -1 if fuel(code,average-1) < fuel(code,average+1) else 1
    current = fuel(code,average)
    i = average + gradient
    while fuel(code,i)< current:
        current = fuel(code,i)
        
        i-=1
    print(fuel(code,i-gradient))
