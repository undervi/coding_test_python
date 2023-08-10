import math

# num보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서 가장 작은 수 구하기!
num = int(input()) 

# 소수 리스트 만들기
n =  1_003_001 # num의 상한값인 1_000_000일 때 나와야 하는 수가 1_003_001이므로 상한값인 n 설정
arr = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1

# num보다 크거나 같은 소수 리스트 만들기
sosu = []
for i in range(num, n+1):
    if i >= 2 and arr[i]:
        sosu.append(i)

# 소수 중에서 팰린드롬인 수 출력        
for i in sosu:
    if str(i) == str(i)[::-1]:
        print(i)
        break