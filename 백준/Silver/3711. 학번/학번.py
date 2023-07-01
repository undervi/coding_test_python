n = int(input())
for _ in range(n):
    num = int(input())
    if num == 1:
        input()
        print(1)
    else:
        st_id = []
        for _ in range(num):
            st_id.append(int(input()))
        
        for i in range(1, 1_000_000):
            result = []
            for st in st_id:
                result.append(st % i)
            if len(set(result)) == len(result):
                print(i)
                break