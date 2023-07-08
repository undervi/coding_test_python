n = int(input())

while n%2 == 0:
    n = n //2
    print(2)

while n > 1:
    for i in range(3, 9_999_999):
        if n%i == 0:
            print(i)
            n = n // i
            break
    
     
        