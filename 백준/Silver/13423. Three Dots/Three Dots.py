import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    points = sorted(list(map(int, input().split())))
    s, e = 0, n-1    
    result = 0

    while s < e:
        length = points[e] - points[s]
        if length % 2 == 0:
            if points[s] + (length//2) in points:
                result += 1
              
        if e > s+1:
            e -= 1
        else:
            e = n-1
            s += 1
    
    print(result)
