#include<math.h>
#include<stdio.h>
#include<string.h>
#define N 50
int palindrome(char mot[N])
{
    int resultat,compteur=0;
    for(int i=0;i<strlen(mot)/2;i++)
    {
        if(mot[i]!=mot[strlen(mot)-i-1])
        {
            resultat=0;
            break;
        }
        else{ compteur=compteur+1;}
    }
    if(compteur==strlen(mot)/2){resultat=1;}
    return resultat;
}
int main()
{ 
    char mot[N];
    printf("\n\tEntrez un mot\t");
    scanf("%s",&mot);
    if(palindrome(mot)==1){printf("\tLe mot '%s' est bien un palindrome\n",mot);}
    else{printf("\tLe mot '%s' n'est pas un palindrome\n",mot);}
    return 0;
}
/*
char mot[N];
    printf("\n\tEntrez un mot\t");
    scanf("%s",&mot);
    int compteur=0;
    for(int i=0;i<strlen(mot)/2;i++)
    {
        if(mot[i]!=mot[strlen(mot)-i-1])
        {
            printf("\tLe mot '%s' n'est pas un palindrome\n",mot);
            break;
        }
        else{ compteur=compteur+1;}
    }
    if(compteur==strlen(mot)/2){printf("\tLe mot '%s' est bien un palindrome\ninte",mot);}
*/