#merge intervals
def f1(a,b):
  s=0
  e=1
  n=[]
  for i in range(1,b):
    if a[i-1][e]>=a[i][s]:
      l=[a[i-1][s],a[i][e]]
      n.append(l)
      a[i]=l
    else:
      l=a[i]
      n.append(l)
  print(n)
 
a=[[1,4],[4,5]]
f1(a,len(a))