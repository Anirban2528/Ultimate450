#Subarray with 0 sum
class Subsum:
    def fun(self,a,b):
        for x in range(0,b):
            self.sum=a[x]
            if self.sum==0:
                return True
            for y in range(x+1,b):
                self.sum+=a[y]
                if self.sum==0:
                    return True
        return False

a=[4,2,-3,1,6]
o=Subsum()
print(o.fun(a,len(a)))