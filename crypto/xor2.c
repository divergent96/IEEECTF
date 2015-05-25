#include<stdio.h>
#include<string.h>
main()
{
int i,n;
char str1[100],str2[100];

printf("String : ");
scanf(" %s",str1);
printf("\nKey : ");
scanf(" %s",str2);

n=strlen(str1);

for(i=0;i<n;i++){
    str1[i]=str1[i]^str2[i%n];
}
printf("\n\n##Cipher text : %s",str1);
}
