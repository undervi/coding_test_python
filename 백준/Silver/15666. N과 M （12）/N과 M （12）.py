import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums = sorted(list(set(nums)))
arr = []

def recur(num, count):
    if count == m:  # 기저 조건
        print(*arr)
        return
      
    for i in range(num, len(nums)):
        arr.append(nums[i])
        recur(i, count+1)
        arr.pop()

recur(0, 0)