/*find max and min kth element in array*/
#include<stdio.h>
int main()
{
 int n,i,k,temp,j;
 int a[n];
 printf("Enter size:");
 scanf("%d",&n);
 for(i=0;i<n;i++)
 {
  printf("Enter element %d:",i);
  scanf("%d",&a[i]);
}
    for (i = 0; i < n-1; i++)      
    for (j = 0; j < n-i-1; j++)  
        if (a[j] > a[j+1])  
        {temp=a[j];
		  a[j]=a[j+1];
		  a[j+1]=temp;  
        }
 printf("Enter the valeue of k:");
 scanf("%d",&k);
 k=k-1;
 printf("MAX k element =%d\nMIN k element =%d\n",a[n-1-k],a[k]);
 return 0;
}