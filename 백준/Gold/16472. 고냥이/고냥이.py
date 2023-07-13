import sys
input = sys.stdin.readline

n = int(input()) # 한계
word = input().rstrip()

s, e = 0, 0
result = 0

record = [word[s]]

while s < len(word) and e < len(word):
    result = max(result, e-s+1)

    if len(record) <= n:
        e += 1
        if e < len(word) and word[e] not in record:
            record.append(word[e])

    if len(record) > n:
        s += 1
        e = s
        record = [word[s]]

print(result)