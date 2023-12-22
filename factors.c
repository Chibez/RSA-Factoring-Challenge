#include <stdio.h>

int main()
{
    long long int number = 239809320265259;
    long int factors1 = 2;
    long int factors2;

    while (number % factors1)
    {
        if (factors1 <= number)
        {
            factors1++;
        }
        else {
            return (-1);
        }
    }

    factors2 = number / factors1;
    printf("%lld = %ld * %ld\n", number, factors2, factors1);
    return (0);
