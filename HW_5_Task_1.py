import collections


def calc_profit_with_col():
    quantity_of_companies = int(input('Введите количество предприятий: '))
    Company = collections.namedtuple('Company', ['name', 'profit'])
    lst_of_comps = []
    for i in range(1, quantity_of_companies + 1):
        name = input('Введите имя: ')
        profit = 0
        for quarter in range(1, 5):
            profit += int(input(f'Доход за {quarter} квартал: '))
        company = Company(name, profit)
        lst_of_comps.append(company)

    average_profit = sum([company.profit for company in lst_of_comps]) / len(lst_of_comps)
    print(f'\nСредняя прибыль организаций за год: {average_profit} руб.\n')

    comps_with_less_than_av = [company for company in lst_of_comps if company.profit < average_profit]
    comps_with_more_than_av = [company for company in lst_of_comps if company.profit > average_profit]
    print(f'Прибыль ниже средней: {comps_with_less_than_av}\n')
    print(f'Прибыль выше средней: {comps_with_more_than_av}\n')


calc_profit_with_col()
