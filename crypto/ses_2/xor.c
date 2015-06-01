//Code still not working.Not getting converted to hexa.


#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void hextochar(char[],char[]);

int main(){
    int i,j,k;
    char strhex[100],strdec[100],keyhex[100],keydec[100],temp[2],out[100];
    
    printf("Input plaintext : ");
    scanf(" %s",strhex);
    printf("Input key : ");
    scanf(" %s",keyhex);
    printf("\nCipher : ");
    
    hextochar(strhex,strdec);
    printf("#\n#strdec = %s\n",strdec);
    hextochar(keyhex,keydec);

    for(i=0;i<strlen(strdec);i++){
        out[i]=strdec[i]^keydec[i%strlen(keydec)];
        sprintf(temp,"%x",out[i]);
        printf("%s",temp);
    }
    printf("\n");

    return(0);
}

void hextochar(char str1[100],char str2[100]){
    int i,j,k;
    char temp[2];
    for(i=0,k=0;i<strlen(str1);i+=2,k++){
        for(j=0;j<2;j++)
            temp[j]=str1[i+j];
        sprintf(temp,"%c",num);
        str2[k]=temp[0];
    }
    str2[k+1]='\0';
}

