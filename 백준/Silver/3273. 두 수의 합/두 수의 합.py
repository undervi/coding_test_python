import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)

sum = int(input())
result = 0

left = 0
right = n-1

while left < right:
    if nums[left] + nums[right] == sum:
        result += 1
        left += 1
        right -= 1
    elif nums[left] + nums[right] > sum:
        right -= 1
    else:
        left += 1
print(result)