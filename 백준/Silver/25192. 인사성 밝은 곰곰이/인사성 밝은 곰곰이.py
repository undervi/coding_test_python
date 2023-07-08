import sys
input = sys.stdin.readline

n = int(input())
ls = set()
result = 0

for _ in range(n):
    name = input().rstrip()
    if name == "ENTER":
        result += len(ls)
        ls.clear()
    else:
        ls.add(name)
    
print(result+len(ls))