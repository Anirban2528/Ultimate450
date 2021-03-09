#Best time to buy and sell stock
class Stock:
    def fun(self,a,b):
        self.p=0
        for x in range(0,b):
            for y in range(x+1,b):
                if (a[y]-a[x])>self.p:
                        self.p=a[y]-a[x]
        return(self.p)

a=[7,1,5,3,6,4]
o=Stock()
print(o.fun(a,len(a)))