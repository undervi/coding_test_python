import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
result = [0 for _ in range(n)]

cnt, idx = 0, 0
while True:
    i = idx%n
    idx += 1
    if seq[i] > 0:
        seq[i] -= 1
        cnt += 1
        if seq[i] == 0:
            result[i] = cnt

    if list(set(seq)) == [0]: # 기저조건
        break
    
print(*result)