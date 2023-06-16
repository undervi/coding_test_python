def solution(x, n):
    answer = []
    
    if x == 0: 
        return [0] * n

    j = x*n+1 if x>0 else x*n-1
    for i in range(x, j, x):
        answer.append(i)
    
    return answer