self_number = list(range(1, 10001))  # 전체 숫자
remove_set = set()

for number in self_number:
    for num in str(number):
        number += int(num)
    remove_set.add(number)    # 생성자인 숫자

for number in self_number:
    if number not in remove_set:
        print(number)