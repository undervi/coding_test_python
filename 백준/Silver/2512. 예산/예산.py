import sys
input = sys.stdin.readline

n = int(input()) # 지방의 수
moneys = list(map(int, input().split())) # 예산 리스트
limit = int(input()) # 총 예산

if sum(moneys) <= limit: # 예산의 합이 총 예산 이하라면
    print(max(moneys)) 
else:
    start, end = limit//n, max(moneys)-1
    
    while start <= end:      
        tot = 0
        mid = (start + end) // 2
        
        # mid 이하인건 그대로, 큰건 mid로 해서 더하기
        for m in moneys:
            if m <= mid:
                tot += m
            else:
                tot += mid    
        
        if tot > limit:
            end = mid-1
        else:
            start = mid+1

    print(end)