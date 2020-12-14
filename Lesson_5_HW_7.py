import json

res_list = []
with open('./pz7.txt', 'r', encoding="utf8") as f_obj:
    company = {}
    aver = 0
    for line in f_obj:
        c = line.split()
        company[c[0]] = int(c[2]) - int(c[3])
        if company[c[0]] > 0:
            aver += company[c[0]]
    print('Компании:', company)
    print('Средняя прибыль:', aver / len(company.keys()))
    res_list = [company, {"average_profit": aver / len(company.keys())}]
with open('./pz7.json', 'w', encoding='utf8') as f_obj:
    json.dump(res_list, f_obj, ensure_ascii=False)
