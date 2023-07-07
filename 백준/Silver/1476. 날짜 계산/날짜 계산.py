import sys
input = sys.stdin.readline

ls = []
e, s, m = map(int, input().split())

for i in range(1, 99999999999):
    if (e == i%15) or (i%15==0 and e==15):
        if (s == i%28) or (i%28==0 and s==28):
            if (m == i%19) or (i%19==0 and m==19):
                print(i)
                break