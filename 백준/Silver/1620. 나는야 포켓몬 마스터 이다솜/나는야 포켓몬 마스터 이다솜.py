import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dogam = {}

for i in range(1, n+1):
    dogam[input().strip()] = i

dogam_list = list(dogam.keys())    
    
for _ in range(m):
    hint = input().strip()
    if hint.isalpha():
        print(dogam[hint])
    else:
        print(dogam_list[int(hint)-1])