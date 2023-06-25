n = int(input())
i_arr = list(map(int, input().split()))
b, c = map(int, input().split())
result = 0

for i in range(len(i_arr)):
  i_arr[i] -= b
  result += 1
  if i_arr[i] > 0:
    result += i_arr[i]//c
    if i_arr[i] % c != 0:
      result += 1

print(result)