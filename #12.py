#To merge two sorted arrays without using any extra space
class Solution:
   def merge(self,arr1,arr2,n,m):
      for x in range(0,min(len(arr1),len(arr2))):
          for j in range(0,max(len(arr1),len(arr2))):
              if arr1[x]>arr2[j]:
                  arr1[x]+=arr2[j]
                  arr2[j]=arr1[x]-arr2[j]
                  arr1[x]-=arr2[j]
      arr1=sorted(arr1)
      arr2=sorted(arr2)
      for x in arr1:
           print(x,end='')
      for x in arr2:
           print(x,end='')
        
a=[10,12]
b=[5,18,10]
o=Solution()
o.merge(a,b,len(a),len(b))