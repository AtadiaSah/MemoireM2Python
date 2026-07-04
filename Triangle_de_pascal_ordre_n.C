#include <stdio.h>                     //<>
#include <stdlib.h>
int main()
{
    int n,i,j;
    printf("\tEntrer un nombre\t");
    scanf("%d",&n);
    int T[n+1][n+1];
    for( i= 0; i <=n; i++)
    {
        T[i][i]=1;
        T[i][0]=1;
        for(j=1; j<i; j++){  T[i][j]=T[i-1][j]+T[i-1][j-1];} 
    }
    // afficharge de la table de pascal
    printf("\tle triangle de pascal est:\n");
    for( i= 0; i<=n; i++)
    {
        for (j= 0; j<=i; j++){
            printf("%d\t",T[i][j]);
        } 
        printf("\n");
    }
 return 0;
}