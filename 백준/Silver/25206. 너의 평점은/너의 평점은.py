import sys
match = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0}
score, count = 0, 0

infor = []
for _ in range(20):
    infor.append(list(sys.stdin.readline().split()))

for i in range(len(infor)):
    if infor[i][2] != 'P':
        count += float(infor[i][1])
        score += (match[infor[i][2]] * float(infor[i][1]))

print(score/count)