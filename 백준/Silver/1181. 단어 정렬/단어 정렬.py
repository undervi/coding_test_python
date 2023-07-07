import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]
words.sort(key=lambda x: (len(x), x))
prints = []

for word in words:
    if word not in prints:
        prints.append(word)
for p in prints:
    print(p)