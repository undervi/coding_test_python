import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
sums = [nums[0]]

for i in range(1, n):
    sums.append(sums[-1]+nums[i])
  
cnt = int(input())
for _ in range(cnt):
    s, e = map(int, input().split())
    print(sums[e-1] if s==1 else sums[e-1] - sums[s-2])