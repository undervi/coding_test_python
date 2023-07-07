import sys
input = sys.stdin.readline

def recur(cnt, num):
    if cnt == m:
        print(num.strip())
        return

    for i in range(1, n+1):
        recur(cnt+1, num+" "+str(i))
  
n, m = map(int, input().split())
recur(0, "")