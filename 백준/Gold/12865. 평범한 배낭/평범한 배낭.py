import sys
sys.setrecursionlimit(99999999)
input = sys.stdin.readline

n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(k+1)] for _ in range(n)]

def recur(idx, weight):
    if weight > k:
        return -999999
    if idx == n:
        return 0
    if dp[idx][weight] != -1:
        return dp[idx][weight]

    # 물건을 넣은 경우, 넣지 않은 경우
    dp[idx][weight] = max(recur(idx+1, weight+items[idx][0]) + items[idx][1], recur(idx+1, weight)) 
    return dp[idx][weight]

ans = recur(0,0)
print(ans)