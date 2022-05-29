# Prints a column of bricks, catching exceptions


def main():
    height = get_height()
    for i in range(height):
        print("#")


def get_height():
    while True:
        try:
            n = int(input("Height: "))
        except ValueError:
            print("That's not an integer!")
        else:
            if n > 0:
                return n


main()
