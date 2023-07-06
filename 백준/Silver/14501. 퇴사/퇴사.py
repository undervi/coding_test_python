n = int(input())
table = [[] for _ in range(n+1)]
dp = [-1 for _ in range(n+1)] # 가장 좋은 것 저장

for i in range(n):
    a, b = map(int, input().split())
    table[i+1] = [a,b] # 0일차는 무시하고 1일차 부터 값이 들어옴

def recur(day):
    # 퇴사날이 지나면 안되게!
    if day > n+1:
        return -999999999999
      
    # 퇴사날이라면 계산해줘
    if day == n + 1:
        return 0

    # 이미 계산된것은 그대로 출력
    if dp[day] != -1:
        return dp[day]

    # 상담을 받거나 안받거나 더 좋은 것 
    dp[day] = max(recur(day+table[day][0]) + table[day][1], recur(day+1))
    return dp[day]

recur(1)
print(max(dp))