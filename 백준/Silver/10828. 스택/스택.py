import sys

n = int(sys.stdin.readline().rstrip())
stack = []

def push(x):
    stack.append(x)

def play(command):
    if command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == 'top' or command == 'pop':
        if len(stack) > 0:
            print(stack[len(stack)-1])
            if command == 'pop':
                stack.pop()
        else:
            print(-1)
  
for _ in range(n):
    command = sys.stdin.readline().rstrip()
  
    if 'push' in command:
        push(command.split()[1])
    else:
        play(command)