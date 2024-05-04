def print_row(spaces, bricks):
    # print spaces
    for _ in range(spaces):
        print(" ", end="")
    # print bricks
    for _ in range(bricks):
        print("#", end="")
    print()


def main():
    # prompt the user for the pyramid's height
    while True:
        try:
            n = int(input("Height: "))
            if n >= 1 and n <= 8:
                break
            else:
                print("Height must be between 1 and 8")
        except ValueError:
            print("Please enter a valid number: ")

    # print a pyramid of that height
    for i in range(n):
        # print rox bricks
        print_row(n - i - 1, i + 1)


if__name__ = "__main__"
main()
