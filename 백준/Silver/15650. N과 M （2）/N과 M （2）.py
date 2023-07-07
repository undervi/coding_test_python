import sys
input = sys.stdin.readline

ls = []
n, m = map(int, input().split())

def sequence(num, cnt):      
    global ls
  
    if cnt == m:
        if sorted(num) not in ls:
            ls.append(sorted(num))
        return
        
    for i in range(n):
        if i+1 not in num:
            sequence(num + [i+1], cnt+1)

sequence([], 0)

for l in ls:
    print(' '.join(str(s) for s in l))