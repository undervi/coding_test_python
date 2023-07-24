# 모든 위치에서
# 모든 체커의 거리를 계산해서
# 가장 적은 값을 알아내자!
# 단, 각 체커의 x좌표와 y좌표는 1,000,000보다 작거나 같은 자연수

# 1번) x, y를 구분해서 계산해준 뒤에 합쳐서 최소값을 구하자
# 2번) 한 곳에서 모일 때 비용을 최소화 하기 위해서는 우리의 위치 중 한 곳에서 모이면 됨!
# 3번) 2명이 만나는 최소 거리를 구할 땐, 만나는 점에서 가장 가까운 두 체커의 거리만 더해주면 된다!


import sys
input = sys.stdin.readline

n = int(input())
arr = []
set_x, set_y = set(), set()
answer = [-1]*n

# 입력받기
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
    set_x.add(a)
    set_y.add(b)
    

# 만날 장소 정하기
for x in set_x:
    for y in set_y:
        dis = []

        # 만날 장소로 각각의 체커들의 거리 계산하기
        for ex, ey in arr:
            dis.append(abs(ex-x)+abs(ey-y))

        # 가까운 순서로 정렬하기
        dis.sort()

        sum_dis = 0
        for i in range(n):
            d = dis[i]
            sum_dis += d
            if answer[i] == -1:
                answer[i] = sum_dis
            else:
                answer[i] = min(sum_dis, answer[i])

print(*answer)