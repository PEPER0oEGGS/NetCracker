"""
Мультислайс (на итераторы)
Написать функцию chain_slice, которая:
1) принимает не менее трёх параметров: два целых числа (start, end) и не менее одной последовательности (итерируемого объекта);
2) возвращает итератор, пробегающий элементы последовательности, являющейся конкатенацией всех переданных в функцию последовательностей
(сначала все элементы из первой последовательности, потом из второй и т.д.), с элемента под номером begin до end - 1 включительно.

Пример:
print(*(chain_slice(17, 33, range(7),  range(8),  range(6),  range(9),  range(5))))

Результат:
2 3 4 5 0 1 2 3 4 5 6 7 8 0 1 2

P.S. если использовать модуль itertools (https://docs.python.org/3/library/itertools)
тело функции можно реализовать в одну небольшую, хорошо читаемую строку =)
"""


def chain_slice(*args):
    """args = (start, stop, iterator1, iterator2, iterator3,...)"""
    iterators = list(args)
    start, stop = iterators[0:2]
    del (iterators[0:2])
    marker = 0
    res = ""
    for iterator in iterators:
        for i in iterator:
            marker += 1
            if (marker > start):
                res += str(i)
                if marker == stop:
                    return res



print(*(chain_slice(17, 33, range(7), range(8), range(6), range(9), range(5))))
