import sys
max = 0
max_string = ""

word = sys.stdin.readline()

for i in range(26):
    count = word.count(chr(i+97)) + word.count(chr(i+65))
    
    if max < count:
        max = count
        max_string = chr(i+65)
    elif max == count:
        max_string = "?"

print(max_string)