n = int(input())
milks = list(map(int, input().split()))
    
result = 0
rule = "012"

for milk in milks:
    if str(milk) == rule[result%3]:
        result += 1

print(result)