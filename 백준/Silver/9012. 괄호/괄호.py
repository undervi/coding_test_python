import sys
input = sys.stdin.readline

n = int(input())
result = ""

for _ in range(n):
    s = input().strip()
    while '()' in s:
        s = s.replace('()', '')
    print("YES" if len(s)==0 else "NO")