import sys

MSG_DIV_BY_0 = "ERROR (div by zero)"
MSG_MOD_BY_0 = "ERROR (modulo by zero)"

if len(sys.argv) < 3:
    print("Usage: python operations.py")
    print("Example:")
    print("    python operations.py 10 3")

elif len(sys.argv) > 3:
    print("InputError: too many arguments")
    print("")
    print("Usage: python operations.py")
    print("Example:")
    print("    python operations.py 10 3")

else:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except:
        print("InputError: only numbers")
        print("")
        print("Usage: python operations.py")
        print("Example:")
        print("    python operations.py 10 3")
    else:
        print("Sum: {}".format(a + b))
        print("Difference: {}".format(a - b))
        print("Product: {}".format(a * b))
        print("Quotient: {}".format((a / b) if b > 0 else MSG_DIV_BY_0))
        print("Remainder: {}".format((a % b) if b > 0 else MSG_MOD_BY_0))
