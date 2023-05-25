import sys
string = sys.stdin.readline().rstrip()

if string == ''.join(reversed(string)):
    print(1)
else:
    print(0)