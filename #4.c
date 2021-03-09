/*To sort an array of 0,1 and 2 without using sorting algo.*/
#include<stdio.h>
void swap(int *a,int *b);
void swap(int *a,int *b)
{
    int t=*a;
    *a=*b;
    *b=t;
}
void main()
{
	int a[]={2,0,1,1,2,0};
	int l=sizeof(a)/sizeof(a[0]);
	int i,mid=0,low=0,hi=l-1,t;
	while(mid<=hi)
    {
        if(a[mid]==0)
			    swap(&a[low++],&a[mid++]);
		else if(a[mid]==1)
			    mid++;
			else
				swap(&a[mid],&a[hi--]);
				
	}
	for(i=0;i<l;i++)
		printf("%d",a[i]);
	
}