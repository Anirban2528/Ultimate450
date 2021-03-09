#Factorial of large num
class fact:
    def fun(self,n):
        if n==0:
            return 1
        else:
            return n*self.fun(n-1)

o=fact()
print(o.fun(int(input())))