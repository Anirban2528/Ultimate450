#To print max sum of subarrays
def f1(a,b):
  maxc=a[0]
  maxe=a[0]
  for i in range(1,b):
    maxc= max(a[i],maxc+a[i])
    maxe= max(maxe,maxc)
  return maxe
 
a=[1,-2,-3,2,-1,5,-4]
print('Max contiguous subarray sum :',f1(a,len(a)))