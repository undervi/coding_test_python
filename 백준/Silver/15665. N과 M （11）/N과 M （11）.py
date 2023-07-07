import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums = sorted(list(set(nums)))
arr = []

def recur(count):
    if count == m:  # 기저 조건
        print(*arr)
        return
      
    for num in nums:
        arr.append(num)
        recur(count+1)
        arr.pop()

recur(0)