import sys
input = sys.stdin.readline

n = int(input())
cal = input().strip()
alpha = {}
stack = []

for i in range(n):
    alpha[chr(65+i)] = int(input())

for i in range(len(cal)):
    if cal[i] not in ["+", "-", "*", "/"]:
        stack.append(alpha[cal[i]])
    else:
        b = stack.pop()
        a = stack.pop()
        if cal[i] == "+":
            stack.append(a+b)
        elif cal[i] == "-":
            stack.append(a-b)
        elif cal[i] == "*":
            stack.append(a*b)
        elif cal[i] == "/":
            stack.append(a/b)

print("{:.2f}".format(stack[0])) 