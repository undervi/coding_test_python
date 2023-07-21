cnt = int(input())
nums = list(map(int, input().split()))

for num in nums:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            cnt -= 1
            break
        
print(cnt if 1 not in nums else cnt-1)