#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void extkey(char [],int);
void lowerstr(char[]);

main(){
    int i,n;
    char instr[100],keystr[100];
//Input step    
    printf("\nThe plaintext : ");
    scanf(" %s",instr);
    printf("\nThe key : ");
    scanf(" %s",keystr);
//Length for later use    
    n=strlen(instr);
//Functions to convert input to lower case
    lowerstr(instr);
    lowerstr(keystr);
//Function to lengthen key to plaintext
    extkey(keystr,n);
//Plaintext to cypher    
    for(i=0;i<n;i++)
        instr[i]=instr[i]+keystr[i]-97;
    
    printf("\nCiphertext : %s\n",instr);
//Cyphertext to plaintext
    for(i=0;i<n;i++)
        instr[i]=instr[i]-keystr[i]+97;

    printf("\nPlaintext : %s\n",instr);
}

//The key lengthening function.
void extkey(char str[],int num){

    int len=strlen(str),i;
    
    if(num==len)
        exit(0);
    
    char temp[100];
    
    for(i=0;i<num;i++)
        temp[i]=str[i%len];
        
    strcpy(str,temp);
}

//String to lowercase function
void lowerstr(char str[]){
    int i;
    
    for(i=0;i<strlen(str);i++)
      str[i]=tolower(str[i]);
}
