rus_nums = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}
nums_rus = []
with open('./pz4.txt', 'r') as f_obj:
    for f_line in f_obj:
        eng_num = f_line.split('-')[0].lower().strip()
        num = f_line.split('-')[1]
        nums_rus.append(f'{rus_nums[eng_num].capitalize()} -{num}')
with open('pz4res.txt', 'w', encoding='utf8') as f_res:
    f_res.writelines(nums_rus)