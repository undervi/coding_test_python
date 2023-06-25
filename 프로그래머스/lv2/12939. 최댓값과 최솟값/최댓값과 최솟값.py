def solution(s):
    num_arr = list(map(int, s.split()))
    num_arr = sorted(num_arr)
    answer = str(num_arr[0]) + ' ' + str(num_arr[len(num_arr)-1])
    return answer