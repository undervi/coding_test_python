from itertools import permutations
    
n = int(input())
result = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))
del_list = []

for _ in range(n):
    number, st, ball = map(int, input().split())
    number = str(number)
    for rs in result:
        rs_num = rs[0]+rs[1]+rs[2]

        # 볼 제거
        a, b, c = 1 if number[0] in rs_num else 0, 1 if number[1] in rs_num else 0, 1 if number[2] in rs_num else 0
        if ball + st != a + b + c:
            del_list.append(rs)
          
        # 스트라이크 제거
        d, e, f = 1 if rs[0] == number[0] else 0, 1 if rs[1] == number[1] else 0, 1 if rs[2] == number[2] else 0
        if st != d + e + f:
            del_list.append(rs)
      

result = [x for x in result if x not in del_list]
print(len(result))