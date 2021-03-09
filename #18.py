#Count pairs with given sum
class Maxpair:
    def fun(self,a,siz,k):
        self.count=0
        for x in range(0,siz):
            for y in range(x+1,siz):
                if (a[y]+a[x])==k:
                        self.count+=1
        return(self.count)

a=[1,5,7,1]
k=6
o=Maxpair()
print(o.fun(a,len(a),k))