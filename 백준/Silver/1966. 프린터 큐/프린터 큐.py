from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
    
    while queue:
        best = max(queue)
        front = queue.popleft()
        m -= 1

        if front == best:
            count += 1
            if m < 0: # m이 0보다 작다는 것은 뽑은 숫자가 내 숫자라는 뜻
                print(count)
                break
            
        else:
            queue.append(front)
            if m < 0: # m이 0보다 작다는 것은 뽑은 숫자가 내 숫자라는 뜻
                m = len(queue) - 1 # 맨 뒤로 이동