#Common elements
class Common:
    def fun(self,a,b,c,n,o,p):
        self.d=[]
        for x in range(0,n):
            if a[x] in b and c:
                if a[x] not in self.d:
                    self.d.append(a[x])
        if len(self.d)==0:
            return(-1)
        else:
            return(self.d)
        
a=[1,5,10,20,40,80]
b=[6,7,20,80,100]
c=[3,4,15,20,30,70,80,120]
ob=Common()
print(ob.fun(a,b,c,len(a),len(b),len(c)))