from random import sample

nums = []

with open('./pz5.txt', 'w') as f_obj:
    nums = sample(range(-20, 10), 10)
    f_obj.write(' '.join(map(str, nums)))
    print('Файл заполнен числами:', nums)
with open('./pz5.txt', 'r') as f_read:
    print('Сумма чисел в файле: ', sum(int(x) for x in f_read.readline().split()))
