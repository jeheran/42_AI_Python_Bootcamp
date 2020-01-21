import sys

try:
    if sys.argv[1].isdigit():
        raise Error()
    int(sys.argv[2])
except:
    print("ERROR")
else:
    oldstring = str(sys.argv[1])
    new_list = []
    for w in oldstring.split(' '):
        if len(w) >= int(sys.argv[2]):
            new_list.append(w)
    print(new_list)
