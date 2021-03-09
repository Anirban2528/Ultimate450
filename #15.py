#Next permutation
class Permu:
  def fun(self,a,b):
    for x in range(b-1,-1,-1):
      for y in range(x-1,b):
        if a[x]>a[y] and y!=b-1:
          a[x]+=a[y]
          a[y]=a[x]-a[y]
          a[x]-=a[y]
          print(a)
          return(a)


a=[3,2,1]
o=Permu()
o.fun(a,len(a))