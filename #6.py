#Find union and intersection of two sorted arrays
def unint(a,b):
 c=a+b
 u=[]
 i=[]
 for x in a:
  if x in a and x in b:
    i.append(x)
 for x in c:
  if x not in u:
    u.append(x)
 print('UNION=',u)
 print('INTERSECTION=',i)

a=[1,2,3,4,5]
b=[1,4,7,8]
unint(a,b)  