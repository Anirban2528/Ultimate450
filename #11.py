#To find duplicate in array of n+1 integers
class Num:
 def dup(self,nums):
  for x in nums:
    if nums.count(x)>1:
      print(x)
      break
a=[1,3,4,2,2]
o= Num()
o.dup(a)