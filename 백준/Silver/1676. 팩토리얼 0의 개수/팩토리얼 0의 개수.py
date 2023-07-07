import sys
input = sys.stdin.readline

n = int(input().strip())

def pac(n):
    if n <= 2:
        return 1 if n==0 else n
    return n * pac(n-1)

result = 0
for pac in str(pac(n))[::-1]:
    if pac == '0':
        result += 1
    else:
        break
print(result)