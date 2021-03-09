#Inversion Count
class Inver:
    def inversioncount(self,a,b):
        self.c=0
        for x in range(0,b):
            for y in range(x+1,b):
                if a[x]>a[y]:
                    self.c+=1
        return(self.c)

arr=[2,4,1,3,5]
o=Inver()
print(o.inversioncount(arr,len(arr)))