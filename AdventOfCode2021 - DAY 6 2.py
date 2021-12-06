def pop(n):
  g = [{6:1,8:1},{0:1},{1:1},{2:1},{3:1},{4:1},{5:1},{6:1},{7:1}]
  d = {n:1}
  for i in range(256):
    dtemp = {}
    for k,v in d.items():
      for ok, ov in g[k].items():
        dtemp[ok] = v*ov if ok not in dtemp else dtemp[ok] + v*ov
    d = dict(dtemp)   
  return sum(d.values())

def fishy(code):
  code = list(map(int,code.replace(",","*").split("*")))
  t256 = [pop(i) for i in range(9)]
  return sum([t256[v] for v in code])
