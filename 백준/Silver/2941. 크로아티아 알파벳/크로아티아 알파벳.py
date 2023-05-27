word = input()
array = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for x in array:
    word = word.replace(x, '*')

print(len(word))