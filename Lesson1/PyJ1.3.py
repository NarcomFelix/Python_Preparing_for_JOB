"""
Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
 “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря
"""
import random

quantity = 4
arr = []
dict_ = {}


for i in range(quantity):
    SIZE = 20
    MIN_ITEM = 1
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    print(array)
    a = min(array)
    b = max(array)

    arr.append(a)
    num = i + 1
    key = "elem_" + str(num)
    dict_[key] = b

print(arr)
print(dict_)




