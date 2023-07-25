a, b = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0 for _ in range(a+1)]

for i in range(a):
    prefix[i+1] = prefix[i] + arr[i]

answer = -999_999_999
for i in range(b, a+1):
    answer = max(answer, prefix[i]-prefix[i-b])

print(answer)