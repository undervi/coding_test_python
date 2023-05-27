import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    array = []
    word = sys.stdin.readline().rstrip()
    for i in range(len(word)):
        if word[i-1] != word[i] and i > 0:
            array.append(word[i-1])
        if word[i] in array:
            n -= 1
            break

print(n)