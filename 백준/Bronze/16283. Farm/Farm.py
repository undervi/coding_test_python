a, b, n, w = map(int, input().split())
result = []

for sheep in range(1, n):
    for goat in range(1, n):
        if sheep + goat == n:
            if a * sheep + b * goat == w:
                result.append([str(sheep), str(goat)])

if len(result) > 1 or len(result) == 0:
    print(-1)
else:
    print(" ".join(result[0]))
