def div(n):
    tmp_n = n
    for i in range(1,99):
        if 2**i > n:
            break
        tmp_n += (n//(2**i)) * (2**(i-1))
    return tmp_n

a, b = map(int, input().split())
a -= 1

print(div(b) - div(a))