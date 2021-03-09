/*Cyclically rotate the array by one*/
#include<stdio.h>
void main()
{
 int a[]={2,4,3,7,6,9};
 int i,l=sizeof(a)/sizeof(a[0]);
 int t=a[l-1],temp=0;
 for(i=l-1;i>0;i--)
 {
     a[i]=a[i-1];
 }
 a[0]=t;
 for(i=0;i<l;i++)
 {
	 printf("%d",a[i]);
 }
}