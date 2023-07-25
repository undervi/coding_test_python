import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def checker(number, hint_idx):
    # check number
    strike = 0
    ball = 0
    A = number // 100               # 100의 자리
    B = (number - A*100) // 10      # 10의 자리
    C = number % 10                 # 1의 자리

    # 힌트
    _number = hint[hint_idx][0]
    _strike = hint[hint_idx][1]
    _ball = hint[hint_idx][2]
    _A = _number // 100             # 100의 자리
    _B = (_number - _A*100) // 10   # 10의 자리
    _C = _number % 10               # 1의 자리

    # ball
    if A == _B or A == _C:
        ball += 1
    if B == _A or B == _C:
        ball += 1
    if C == _A or C == _B:
        ball += 1

    # strike
    if A == _A:
        strike += 1
    if B == _B:
        strike += 1
    if C == _C:
        strike += 1

    # ball_cnt와 strike_cnt가 hint와 일치하는지 여부 리턴
    return ball == _ball and strike == _strike

def recur(hint_idx, number):
    global answer 

    # 기저 조건
    if number == 1000:
        return

    # 조건에 맞는 숫자만 진행
    num_arr = list(map(int, str(number)))
    if len(set(num_arr)) == 3 and 0 not in num_arr: 
    
        # 힌트에 모두 통과했다면 answer에 1 더해주고 다음 숫자 진행
        if hint_idx == n:
            answer += 1
            recur(0, number+1)
            return
        
        # 힌트에 통과했다면 힌트 번호 올리기
        if checker(number, hint_idx):
            recur(hint_idx+1, number)
        # 만약에 힌트에 통과하지 않았다면 -> 다음 숫자 진행
        else:
            recur(0, number+1)

    # 조건에 맞지 않다면 다음 숫자로 넘기기
    else:
        recur(0, number+1)

n = int(input())
hint = [list(map(int, input().split())) for _ in range(n)]
answer = 0

recur(0, 100)
print(answer)