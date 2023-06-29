n = int(input())

for _ in range(n):
    number = int(input())
    result = ""
  
    for i in range(2, 1_000_001):
        if number % i == 0:
            result = "NO"
            break
            
    if result == "NO":
        print("NO")
    else:
        print("YES")