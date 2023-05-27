import sys

table = [sys.stdin.readline().rstrip() for _ in range(5)]
string = ""

for j in range(15):
    for i in range(5):     
        if len(table[i]) > j:  
            string += table[i][j]

print(string)