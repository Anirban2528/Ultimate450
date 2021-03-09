#include<stdio.h>
void main()
{
	int a[]={10,20,30,40};
	int l=sizeof(a)/sizeof(a[0]);
	int b[sizeof(a)];
	int i=0;
	while(i!=l)
	{
		b[i]=a[l-i-1];
		i++;
	}
	for(i=0;i<l;i++)
	{
		printf("%d\n",b[i]);
}}