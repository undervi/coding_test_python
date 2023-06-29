n = int(input())
home_arr = list(map(int, input().split()))
home_arr.sort()        
print(home_arr[(n-1)//2])