#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main (void)
{
    //prompt the user for change owed, in cents
    int cents = get_cents();

    //calculate how many queartes you should give customer
    int quarters = calculate_quarters(cents);

    //substract the value of those quearters from remaining cents
     cents = cents - quarters * 25;

    //calculare how many dimes you should give customer
    int dimes = calculate_dimes(cents);
    //subtract the value of those dimes from remaining cents
    cents = cents - dimes * 10;

    //calculate how many nickels you should give customer
    int nickels = calculate_nickels(cents);
    //substract the value of those nickels from remaining cents
    cents = cents - nickels * 5;

    //calculate how many pennies you should give customer
    int pennies = calculate_pennies(cents);
    //substract the value of those pennies from remaining cents
    cents = cents - pennies * 1;

    //sum the numer of quearters, dime, nickels, and pennies used
    int coins = quarters + dimes + nickels + pennies;
    //print that sum
    printf("%i\n", coins);
}

int get_cents (void)
{
    int cents;
    do
    {
    cents = get_int("Change Owed: ");
    }
    while (cents < 0);
    return cents;
}

int calculate_quarters (int cents)
{
    int quarters = 0;
    while(cents >= 25)
    {
        cents = cents - 25;
        quarters++;
    }
    return quarters;
}

int calculate_dimes(int cents)
{
    int dimes = 0;
    while(cents >=10)
    {
        cents = cents - 10;
        dimes++;
    }
    return dimes;
}

int calculate_nickels(int cents)
{
    int nickels = 0;
    while(cents >= 5)
    {
        cents = cents - 5;
        nickels++;
    }
    return nickels;
}

int calculate_pennies(int cents)
{
    int pennies = 0;
    while(cents >=1)
    {
        cents = cents - 1;
        pennies++;
    }
    return pennies;
}
