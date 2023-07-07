import sys
input = sys.stdin.readline

s = input().strip()
rule = ["pi", "ka", "chu"]

s = s.replace("pi", "*")
s = s.replace("ka", "*")
s = s.replace("chu", "*")
s = s.replace("*", "")

print("YES" if len(s)==0 else "NO")