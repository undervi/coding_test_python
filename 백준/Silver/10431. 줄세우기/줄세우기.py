import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    count = 0
    
    for i in range(2, 21):
        for j in range(1, i):
            if arr[j] > arr[i]:
                tmp = arr[i]
                for k in range(i-1, j-1, -1):
                    arr[k+1] = arr[k]
                count += (i-j)
                arr[j] = tmp
    
    print(arr[0], count)