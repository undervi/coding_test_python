n, m = map(int, input().split())
# n은 숫자의 범위
# m은 몇번 반복할지

def recur(count, number):
    if count == m:  # 기저 조건
        print(number.lstrip())
        return
      
    for i in range(1, n+1):
        if str(i) not in number:
            recur(count+1, number+" "+str(i))

recur(0, "")