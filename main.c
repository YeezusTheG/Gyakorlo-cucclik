#include <stdio.h>
int main()
{
    long int num, count, sum = 1;

    printf("Enter a positive integer: ");
    scanf("%li", &num);

    for(count = 1; count <= num; ++count)
    {
        sum *= count;
    }

    printf("Sum = %li\n", sum);

    int i = 1;
    while (i <= 10){
        printf("%d\n",i);
        ++i;/* code */
    }
    return 0;
}
