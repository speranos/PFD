import sys


def main():
    user_input = None
    if len(sys.argv) == 1:
        while True:
            user_input = input("Please enter a string: ")
            if user_input:
                break
    if len(sys.argv) != 2 and user_input is None:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)
    if user_input:
        argv = user_input
    else:
        argv = sys.argv[1]
    upper = 0
    lower = 0
    symbol = 0
    space = 0
    digit = 0
    try:
        for char in argv:
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
            elif char.isspace():
                space += 1
            elif char.isdigit():
                digit += 1
            else:
                symbol += 1
    except ValueError:
        print("AssertionError: argument is not a string")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(symbol, "punctuation marks")
    print(space, "spaces")
    print(digit, "digits")


if __name__ == "__main__":
    main()
