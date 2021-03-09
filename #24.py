#longest consecutive subsequence
class Subsq:
  def fun(self,a,n):
    self.c=0
    a.sort()
    for x in range(0,n):
      if x==n-1 or a[x]+1 ==a[x+1]:
          if x>0 and a[x]-1==a[x-1]:
              self.c+=1
          elif x==0 or x==n-1:
              self.c+=1
    return(self.c)

#a=[2,6,1,9,4,5,3]
a=[1,9,3,10,4,20,2]
o=Subsq()
print(o.fun(a,len(a)))