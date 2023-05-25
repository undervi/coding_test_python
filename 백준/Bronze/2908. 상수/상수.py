import sys

a, b = sys.stdin.readline().split()
rev_a = int(''.join(reversed(a)))
rev_b = int(''.join(reversed(b)))

print(max(rev_a, rev_b))