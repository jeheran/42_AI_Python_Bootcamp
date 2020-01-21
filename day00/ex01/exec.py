import sys

string = ' '.join(sys.argv[1:])
string = string[::-1]
final = ''

for l in string:
    val = ord(l)

    if val >= 65 and val <= 90:
        val += 0x20
    elif val >= 97 and val <= 122:
        val -= 0x20
    final += chr(val)
if len(sys.argv) > 1:
    print(final)
