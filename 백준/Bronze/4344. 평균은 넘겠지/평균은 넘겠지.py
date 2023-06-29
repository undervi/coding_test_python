import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    array = list(map(int, sys.stdin.readline().split()))
    count = array[0]
    array.remove(array[0])
    av = sum(array) / count
    av_cnt = 0
    
    for x in array:
        if x > av:
            av_cnt += 1
          
    result = round(av_cnt/count * 100, 3)
    print(f"{result}%")