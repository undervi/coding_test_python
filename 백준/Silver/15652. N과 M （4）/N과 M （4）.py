import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

def recur(num, count):
    if count == m:  # 기저 조건
        print(*arr)
        return
      
    for i in range(num, n+1):
        arr.append(i)
        recur(i, count+1)
        arr.pop()

recur(1, 0)