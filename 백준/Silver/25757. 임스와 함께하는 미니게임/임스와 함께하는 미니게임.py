import sys
input = sys.stdin.readline

n, game = input().split()
num = 1 if game == "Y" else 2 if game == "F" else 3
names = set()

for _ in range(int(n)):
    names.add(input().strip())

print(len(names)//num)