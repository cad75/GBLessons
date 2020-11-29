products = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]
res_dick = {}
attr_keys = products[0][1].keys()
for k in attr_keys:
    res_dick[k] = []
    for p in products:
        res_dick[k].append(p[1][k])
    res_dick[k] = list(set(res_dick[k]))
print(res_dick)