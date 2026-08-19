import sys

if len(sys.argv) != 2:
    print("AssertionError: more than one argument is provided")
    sys.exit(1)
try:
    number = int(sys.argv[1])
    if number % 2 == 0:
        print("I'm even!")
    else:
        print("I'm odd!")
    sys.exit(1)
except ValueError:
    print("AssertionError: argument is not an integer")



