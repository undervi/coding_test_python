import sys

string = sys.stdin.readline().rstrip()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

for x in string:
    for i in range(len(dial)):
        if x in dial[i]:
            result += (i+3)

print(result)