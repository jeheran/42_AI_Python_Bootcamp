import sys

if len(sys.argv) > 2:
    print("ERROR")
else:
    if len(sys.argv) != 1:
        try:
            n = int(sys.argv[1])
        except:
            print("ERROR")
        else:
            if n == 0:
                print("I'm Zero.")
            elif n % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
