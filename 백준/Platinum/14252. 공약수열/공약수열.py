def _gcd(a, b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b

n = int(input())
arr = sorted(list(map(int, input().split())))
cnt = 0

for i in range(n-1):
    # 두 수의 최대 공약수가 1이라면 OK
    if _gcd(arr[i], arr[i+1]) == 1:
        continue

    # 두 수의 최대 공약수가 1이 아니라면 NO
    else:
        # 숫자를 1개 추가하거나
        # 2개 추가해야 함
        # 숫자를 하나씩 올려가면서 양쪽 모두 최대 공약수가 1이 되는 수가 있는지 찾자!
        for j in range(arr[i], arr[i+1]):
            if _gcd(arr[i], j) == 1 and _gcd(arr[i+1], j) == 1:
                cnt += 1
                break
                cnt += 2
            if j == arr[i+1]-1:
                cnt += 2

print(cnt)