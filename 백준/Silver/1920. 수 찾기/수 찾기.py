n = int(input())
arr1 = sorted(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))

for number in arr2:
    s = 0
    e = n-1
    result = 0

    while s <= e: # 같은 경우에도 확인해줘야 함
        mid = (s + e) // 2

        if arr1[mid] == number:
            result = 1
            break

        if arr1[mid] < number: # 업
            s = mid + 1
        else:
            e = mid - 1
    
    print(result)