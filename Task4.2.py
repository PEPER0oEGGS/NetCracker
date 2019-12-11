"""
Статистика вызовов функций (на декораторы и генераторы)

Написать генератор-декоратор(!) stat_counter, который конструирует объекты (назовём пока statistic), такие что:
- первый вызов next(statistic) (он же statistic.send(None)) возвращает словарь, в котором stat будет хранить информацию
 вида { функция: количество вызовов }, где функция — это исходный (не обёрнутый) объект-функция.
- все последующие вызовы statistic.send(function) оборачивают вызов произвольной функции function увеличением
 на 1 соответствующего элемента словаря.
Глобальными именами пользоваться нельзя

Пример:
statistic = stat_counter()
function_calls_statistic = next(statistic)

@statistic.send
def f1(a): return a + 1

@statistic.send
def f2(a, b): return f1(a) + f1(b)

print(f1(f2(2, 3) + f2(5, 6)))
print(function_calls_statistic)

Результат:
21
{<function f1 at 0x7fab8d583950>: 5, <function f2 at 0x7fab8d583a60>: 2}

P.S. В моём решении stat_counter занимает всего 10 строчек, но можно и меньше. Помните о позднем связывании.
"""

def stat_counter(f):
    functions={}
    if f in functions.keys():
        functions[f]+=1
    else:
        functions[f]=1

statistic = stat_counter()
function_calls_statistic = next(statistic)

@statistic.send
def f1(a): return a + 1

@statistic.send
def f2(a, b): return f1(a) + f1(b)

print(f1(f2(2, 3) + f2(5, 6)))
print(function_calls_statistic)
