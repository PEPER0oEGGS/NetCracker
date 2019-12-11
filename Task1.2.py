"""
Task 01: Минимальная функция (на функции и функциональное программирование)

Условие:
Написать функцию get_min_function(), которая:
1) принимает числовую последовательность sequence (любой итерируемый объект, возращащий int или float) и одну или несколько функций;
2) возвращает одну из переданных функций, сумма значений которой на всех элементах в sequenbce наименьшая,
если таких функций несколько, последнюю (по порядку последовательности функций) из них.

Пример:
from math import *
print(get_min_function(range(-2,10), sin, cos, exp)(1)

Результат: 0.8414709848078965
"""
from math import *
import functools

def get_min_function(*args):
    """ args = (interval, function1, function2, function3,...)"""
    function = list(args)
    interval = function.pop(0)
    slove = []
    for f in function:
        slove.append(sum(map(f, interval)))
    return function[slove.index(min(slove))]


print(get_min_function(range(-2, 10), sin, cos, exp)(1))

