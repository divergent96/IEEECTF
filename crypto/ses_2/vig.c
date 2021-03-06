#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void extkey(char [],int);
void lowerstr(char[]);
void vigenere(char[],char[],int);

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
    vigenere(instr,keystr,0);    
    
    printf("\nCiphertext : %s\n",instr);
//Cyphertext to plaintext
    vigenere(instr,keystr,1);

    printf("\nPlaintext : %s\n",instr);
}
//Vigenere two way cipher function.
void vigenere(char base[],char key[],int flag){
    int i,n=strlen(base);
    
    if(flag==0)//for plain to cipher
        for(i=0;i<n;i++)
            base[i]=base[i]+key[i]-97;
    else//for cipher to plain
        for(i=0;i<n;i++)
            base[i]=base[i]-key[i]+97;
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
