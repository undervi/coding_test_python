import sys
input = sys.stdin.readline

n = int(input())
s = []

for _ in range(n):
    arr = input().split()
    order = arr[0]
    if len(arr) > 1:
        num = int(arr[1])

    if order == "all":
        s = [i for i in range(1, 21)]
    elif order == "empty":
        s.clear()
    else:
        if int(num) not in s:
            if order == "check":
                print(0)
            elif order == "add" or order == "toggle":
                s.append(int(num))
        else:
            if order == "check":
                print(1)
            elif order == "remove" or order == "toggle":
                s.remove(int(num))