import sys
input = sys.stdin.readline

nums = list(input().rstrip())
nums.sort(reverse=True)
print(''.join(nums))