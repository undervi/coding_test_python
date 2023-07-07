import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
arr = []

def recur(num, count):
    if count == m:  # 기저 조건
        print(*arr)
        return
      
    for i in range(num, n):
        if nums[i] not in arr:
          arr.append(nums[i])
          recur(i+1, count+1)
          arr.pop()

recur(0, 0)