
def get_cents():
    while True:
        try:
            cents = round(float(input("Change Owed: ")) * 100)
            if cents >= 0:
                return cents
            else:
                print("Change owed must be a non-negative interger")
        except ValueError:
            print("Please enter a valid interger")


def calculate_coins(cents, coin_value):
    coins = 0
    while cents >= coin_value:
        cents -= coin_value
        coins += 1
    return coins


def main():
    # prompt the user for change owed, in cents
    cents = get_cents()

    # calculate how many queartes you should give customer
    quarters = calculate_coins(cents, 25)
    cents -= quarters * 25

    # calculare how many dimes you should give customer
    dimes = calculate_coins(cents, 10)
    cents -= dimes * 10

    # calculate how many nickels you should give customer
    nickels = calculate_coins(cents, 5)
    cents -= nickels * 5

    # calculate how many pennies you should give customer
    pennies = cents

    # sum the numer of quearters, dime, nickels, and pennies used
    total_coins = quarters + dimes + nickels + pennies
    # print that sum
    print(int(total_coins))


if__name__ = "__main__"
main()
