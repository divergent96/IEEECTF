#include<stdio.h>
#include<string.h>
main()
{
char str1[100],str2[100],temp[3];
unsigned int st1[100],st2[100];

void hexc(char [];unsigned int []);

printf("String : ");
scanf(" %s",str1);
printf("\nKey : ");
scanf(" %s",str2);


n=strlen(str1);
n2=strlen(str2);


for(i=0;i<n;i++){
    str1[i]=str1[i]^str2[i%n2];
}
printf("\n\n##Cipher text : %s",str1);
}

void hexc(char input[],unsigned int hex[]){
    
    char temp[2];
    int i,j,k,n=strlen(input);
    
    
    for(i=0,k=0;i<n;i++,k++){
        for(j=0;j<2;j++){
            temp[j]=input[i+j]
            }
        hex[i]=
