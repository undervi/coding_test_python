def recur(num):
    if num == m:
        print(*arr)
        return

    for i in range(1, n+1):
        arr.append(i)
        recur(num+1)
        arr.pop()

# n은 숫자의 범위 (1~n), m은 반복할 횟수
n, m = map(int, input().split())
arr = []

recur(0)
