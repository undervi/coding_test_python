import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, max(arr)
cutting = (start+end)//2

while start <= end:
    get = 0
    for i in range(n):
        if arr[i] > cutting:
            get += arr[i]-cutting
    
    if get == m:
        # 나무가 딱 원하는 만큼 나오면 멈추기
        break

    if get < m:
        # 나무가 더 필요하면 자르는 선을 낮춰야 함
        end = cutting - 1

    if get > m:
        # 나무가 너무 많으면 자르는 선을 높여야 함
        start = cutting + 1

    cutting = (start+end)//2

print(cutting)