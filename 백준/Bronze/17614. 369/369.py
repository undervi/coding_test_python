n = int(input())
cnt = 0
    
for i in range(1, n+1):
    for j in str(i):
        if j == '3' or j == '6' or j == '9':
            cnt += 1
print(cnt)