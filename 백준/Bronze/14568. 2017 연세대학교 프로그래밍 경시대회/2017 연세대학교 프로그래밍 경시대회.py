n = int(input())
answer = 0

for th in range(1, n):
    for yh in range(1, n):
        for ng in range(1, n):
            if th + yh + ng == n:
                if ng >= yh + 2:
                    if th % 2 == 0:
                        answer += 1

print(answer)
            