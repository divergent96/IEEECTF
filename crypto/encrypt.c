//Used some website program to check the answer.Encrypt working properly.

#include<stdio.h>
#include<string.h>

main()
  {
    char str1[100],str2[100],ans[100];
//    int ans[100];
    
    printf("Input the string : ");
    scanf(" %s",str1);
    printf("\nEnter key : ");
    scanf(" %s",str2);
    
    int n=strlen(str1);
    int i;
    
    for(i=0;i<n;i++){
        ans[i]=str1[i]^str2[i];
        printf("%03d",ans[i]);

        }
    
     printf("\n##Counter=%d##\n",i);

        
  }
