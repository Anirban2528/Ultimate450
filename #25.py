#Find elements that appear n/k times
class Appear:
  def fun(self,a,n,k):
    a.sort()
    self.s=[]
    for x in range(0,n):
      if a.count(a[x])>n/k:
        if a[x] not in self.s:
          self.s.append(a[x])
    return self.s

a=[3,1,2,2,1,2,3,3]
k=4
o=Appear()
print(o.fun(a,len(a),k))   