n = int(input())
answer = 0

for i in range(2, n):
    answer += i * (n//i - 1)

print(answer%1_000_000)