import sys
input = sys.stdin.readline

while True:
    sen = input().rstrip()
    if sen == ".":
        break

    sentence = ""
    for s in sen:
        if s == '(' or s == ')' or s == '[' or s == ']':
            sentence += s

    while '()' in sentence or '[]' in sentence:
        sentence = sentence.replace('()', '')
        sentence = sentence.replace('[]', '')

    print("yes" if len(sentence)==0 else "no")