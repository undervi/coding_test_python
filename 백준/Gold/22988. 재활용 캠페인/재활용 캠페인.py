import sys
input = sys.stdin.readline

n, max_num = map(int, input().split())
arr = sorted(list(map(int, input().split())))
cnt = 0

# max_num 이상인 것 배열에서 없애기 (cnt+1 해주기)
for i in range(n-1, -1, -1):
    if arr[i] == max_num:
        arr.pop(); 
        cnt += 1
    else:
        break

s, e = 0, len(arr)-1
remain = 0

while s <= e:
    if s == e or arr[s] + arr[e] < max_num/2:
        remain += 1
        s += 1
    else:
        s += 1
        e -= 1
        cnt += 1

print(cnt + remain//3)