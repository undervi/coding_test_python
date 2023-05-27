import sys

remain = set()
for _ in range(10):
    num = int(sys.stdin.readline().rstrip())
    remain.add(num % 42)

print(len(remain))