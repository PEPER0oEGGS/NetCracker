"""
Фиксированная точность (на замыкания-декораторы)
Написать функцию - параметрический декоратор fix_float(presision), который:
1) принимает один целочисленый аргумент - заданную точность;
2) заменяет все вещественные(как позиционные, так и именные) параметры произвольной декорируемой функции, а также её
возвращаемое значение, округляя их до n - го знака после запятой, где n - заданная точность;
3) не вещественные параметры функции и возвращаемые значения
не меняются.

Пример:

@fix_float(4)
def strange_multiplier(*args, mult=0):
    return sum(args) * args[mult]

print(strange_multiplier(0.451235421901, 1.12312342121, 2.523412E-2, 4, mult=-3))

@fix_float(2)
def add_greeting(greeting, number):
    return f'{greeting}, {number}!'

print(add_greeting('Hi', 10.4567))

Результат:
6.2888
Hi, 10.46!
"""


def fix_float(presision):
    def decorator(f):
        def wraper(*args, **kwargs):
            args_pres = []
            for i in args:
                if type(i) is float:
                    args_pres.append(round(i, presision))
                else:
                    args_pres.append(i)
            args_pres = tuple(args_pres)
            res = f(*args_pres, **kwargs)
            if type(res) is float:
                return round(res, presision)
            else:
                return res

        return wraper

    return decorator


@fix_float(4)
def strange_multiplier(*args, mult=0):
    return sum(args) * args[mult]


print(strange_multiplier(0.451235421901, 1.12312342121, 2.523412E-2, 4, mult=-3))


@fix_float(2)
def add_greeting(greeting, number):
    return f'{greeting}, {number}!'


print(add_greeting('Hi', 10.4567))
