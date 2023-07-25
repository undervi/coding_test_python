# GCD(최대 공약수)와 LCM(최소 공배수)

# 1. 갭을 줄여도 된다!
# 예) GCD(8, 12) = GCD(12-8, 8) = GCD(4, 8)
# 예) GCD(30, 36) = GCD(36-30, 30) = GCD(6, 30)

# 2. b % a == 0일 때 (단, a<b) 작은 수가 최대 공약수이다!

gcd, lcm = map(int, input().split())
mul_ab = gcd * lcm

def _gcd(a, b):
    while a % b != 0 : 
        tmp = a % b
        a = b
        b = tmp
    return b

def _lcm(a, b):
    return a*b//gcd

answer = []
for i in range(gcd, int(mul_ab**0.5) + 1, gcd):
    if _gcd(i, mul_ab//i) == gcd and _lcm(i, mul_ab//i) == lcm:
        answer.append([i, mul_ab//i])

print(*answer[-1])