import sys
input = sys.stdin.readline

n = int(input())
a, b, c, d = map(int, input().split())
ingre = [ list(map(int, input().split())) for _ in range(n) ]
money = 999_999_999_999
used, answer_used = [], []

def recur(idx, A, B, C, D, E):
    global money, used, answer_used

    if A >= a and B >= b and C >= c and D >= d: # 모든 필수 영양소를 충족 했다면
        if money > E:   # 기존 비용보다 적다면
            money = E
            answer_used.clear()
            for i in used:
                answer_used.append(i)
    if idx == n:
        return

    # 재료를 사용하는 경우
    used.append(idx+1)
    recur(idx+1, A + ingre[idx][0], B + ingre[idx][1], C + ingre[idx][2], D + ingre[idx][3], E + ingre[idx][4])
    used.pop()
    # 재료를 사용하지 않는 경우
    recur(idx+1, A, B, C, D, E)

recur(0, 0, 0, 0, 0, 0)

answer_used.sort()
if answer_used:
    print(money)
    print(*answer_used)
else:
    print(-1)