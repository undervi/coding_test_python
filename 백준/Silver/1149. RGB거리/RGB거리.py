import sys
input = sys.stdin.readline

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

for idx in range(1, n):
    for RGB in range(3):
        if RGB == 0:    # RED
            dp[idx][RGB] += min(dp[idx-1][1], dp[idx-1][2])
        if RGB == 1:    # GREEN
            dp[idx][RGB] += min(dp[idx-1][0], dp[idx-1][2])
        if RGB == 2:    # BLUE
            dp[idx][RGB] += min(dp[idx-1][0], dp[idx-1][1])

print(min(dp[n-1]))