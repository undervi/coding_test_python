import sys
input = sys.stdin.readline

n = int(input())
rule = ['A', 'B', 'C', 'D', 'E', 'F']

for _ in range(n):
    word = input().strip()
    result = "Good"
  
    # 시작 조건
    if word[0] in rule:
        word = word[1:] if word[0] != 'A' else word
        # 마지막 조건
        if word[-1:] in rule:
            word = word[:-1] if word[-1:] != 'C' else word
            # A 조건
            if word[0] == 'A':
                # 다른글자가 나오기 전까지 나오는 A는 다 없애준다
                word = word[1:]
                while word[0] == 'A':
                    word = word[1:]
                    
                # F 조건
                if word[0] == 'F':
                    # 다른글자가 나오기 전까지 나오는 F는 다 없애준다
                    word = word[1:]
                    if len(word) > 1:
                        while word[0] == 'F':
                            word = word[1:]
                      
                    # C 조건
                    if word[0] == 'C':
                        word = word.replace("C", "")
                        if len(word) == 0:
                            result = "Infected!"
                        
    print(result)