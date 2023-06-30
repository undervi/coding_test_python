import math
a, b, c, number = map(int, input().split())

if a==1 | number % a == 0 | number % b == 0 | number % c == 0:
    print(1)
else:
    result = 0
    for i in range(math.ceil(number/a)):
        for j in range(math.ceil(number/b)):
            for k in range(math.ceil(number/c)):
                if a*i + b*j + c*k == number:
                    result = 1
                    break
            if result == 1:
                break
        if result == 1:
            break
          
    print(result)