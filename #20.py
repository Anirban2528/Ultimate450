#Rearrange array in alternating positive and negative
class Rearrange:
    def fun(self,a,n):
        for x in range(0,n):
            if (a[x] >= 0 and x%2==0):
                    for y in range(x+1,n):
                        if a[y]<0:
                            a[x]+=a[y]
                            a[y]=a[x]-a[y]
                            a[x]-=a[y]
                            break
            elif a[x]<0 and x%2!=0:
                    for y in range(x+1,n):
                        if a[y]>0:
                            a[x]+=a[y]
                            a[y]=a[x]-a[y]
                            a[x]-=a[y]
                            break
        return(a)

#a=[2,1,3,-4,-1,4]            
a=[-5,-2,5,2,4,7,1,8,0,-8]
ob=Rearrange()
print(ob.fun(a,len(a)))