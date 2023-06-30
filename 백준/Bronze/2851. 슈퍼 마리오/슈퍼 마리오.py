result = 0
new_result = 0

for _ in range(10):
    new_result += int(input())

    if abs(100-result) >= abs(100-new_result):
        result = new_result
    
print(result)