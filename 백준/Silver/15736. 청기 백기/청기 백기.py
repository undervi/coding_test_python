n = int(input())
num = 1

while True:
    if num*num > n:
        break
    num += 1

print(num-1)