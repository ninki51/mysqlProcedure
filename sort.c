#include <stdlib.h>
#include <stdio.h>

#include "time.h"
int main(int arg,char **argv)
{
    clock_t start_time = clock();
    int data[3000];
    int i;
    int length=sizeof(data)/sizeof(int);
    for(i=0; i<length;i++)
    {
        data[i] = rand()%10000+1;
    }
    int j,temp;
    for(i=0;i<length;i++)
    {
        for(j=0;j<length-1-i;j++)
        {
            if(data[j] > data[j+1])
            {
                temp = data[j];
                data[j] = data[j+1];
                data[j+1] = temp;
            }
        }
    }

   /* for(i=0;i<length;i++)
    {
        printf("%d\n",data[i]);
    }*/
    clock_t end_time = clock();
    float  time = (double)(end_time-start_time)/CLOCKS_PER_SEC;
    printf("use time: %f",time);
    return 0;
}
