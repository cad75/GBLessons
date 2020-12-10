# -*- coding: utf-8 -*-
from sys import argv


def result(hours, celary, bonus):
    return (hours * celary) + bonus


script_name, time_work, celary_worker, bonus_work = argv

print("Name action: ", script_name)
print("Enter time: ", time_work)
print("Enter celary: ", celary_worker)
print("Enter bonus: ", bonus_work)
print("Total: ", result(int(time_work), int(celary_worker), int(bonus_work)))
