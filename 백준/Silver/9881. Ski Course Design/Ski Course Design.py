import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for i in range(n)])
costs = []

for min_num in range(min(arr), max(arr)-16):
    cost = 0
    max_num = min_num + 17
  
    for num in arr:
        if num < min_num:
            cost += (min_num-num)**2
        elif num > max_num:
            cost += (num-max_num)**2
    costs.append(cost)
  
print(min(costs) if len(costs)>0 else 0)