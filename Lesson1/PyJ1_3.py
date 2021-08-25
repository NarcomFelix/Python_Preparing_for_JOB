"""
Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
 “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря
"""
import random

# 1. Что такое разработать генератор?
# 2. А вот куда передавать начальное и конечное число? Я одно в список, другое в словарь
# А вообще криво получилось
def quant(quantity):
    arr = []
    dict_ = {}

    for i in range(quantity):
        SIZE = 20
        MIN_ITEM = 1
        MAX_ITEM = 100
        array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
        print(array)
        a = array[0]
        b = array[SIZE-1]

        arr.append(a)
        num = i + 1
        key = "elem_" + str(num)
        dict_[key] = b

    print(arr)
    print(dict_)

quant(4)


