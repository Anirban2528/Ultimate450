/*find max and min element in array*/
#include<stdio.h>
int main()
{
 int n,max,min,i;
 printf("Enter size:");
 scanf("%d",&n);
 int a[n];
 for(i=0;i<n;i++)
 {
  printf("Enter element %d:",i);
  scanf("%d",&a[i]);
 }
 max=a[0];
 min=a[0];
 for(i=0;i<n;i++)
 {
  if(a[i]>max)
   max=a[i];
  if(a[i]<min)
   min=a[i];
 }
 printf("MAX =%d\nMIN =%d",max,min);
 return 0;
}