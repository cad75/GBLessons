with open('./pz6.txt', 'r', encoding='utf8') as f_obj:
    res = {}
    for line in f_obj:
        name = line.split(':')[0].strip()
        int_hours = 0
        str_hour = ""
        for char in line.split(':')[1].strip():
            if char.isdigit():
                str_hour += char
            elif str_hour:
                int_hours += int(str_hour)
                str_hour = ""
        res[name] = int_hours
    print(res)