#Minimize the maximum difference between heights
def f1(a,siz,k):
  for x in range(0,siz):
    if (a[x]-k)<1:a[x]+=k
    else:a[x]-=k
  return max(a)-min(a)
a=[3,9,12,16,20]
k=3
print(f1(a,len(a),k))