n = int(input())
ingre = [[] for _ in range(n)]
result = 9999999  #큰 값 저장

for i in range(n):
    a, b = map(int, input().split())
    ingre[i] = [a,b]
  
def recur(idx, sin, ssun, cnt):
    global result
  
    if cnt != 0:
        result = min(result, abs(sin - ssun))
  
    # 기저 조건
    if idx == n:
        return
      
    # 재료를 사용하지 않았을 때
    recur(idx+1, sin, ssun, cnt)
    # 재료를 사용했을 때
    recur(idx+1, sin*ingre[idx][0], ssun+ingre[idx][1], cnt+1)


recur(0, 1, 0, 0)
print(result)