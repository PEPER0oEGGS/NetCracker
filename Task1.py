"""
Палиндром
Ввести целое положительное число и проверить, является ли оно палиндромом,
т. е. совпадает ли первая цифра с последней, вторая — с предпоследней и т. д.
Представлять число в виде последовательности (строки, списка и т. п.) нельзя.
Вывести YES или NO соответственно.
Лидирующие нули не учитывать (числа, заканчивающиеся на 0 — автоматически не палиндромы).

Example:
Input: 1234321
Output: YES
"""
check_number = int(input())
buffer = check_number
reverse_number = 0

while buffer > 0:
    reverse_number = reverse_number * 10 + buffer % 10
    buffer //= 10

if reverse_number == check_number:
    print("YES")
else:
    print("NO")
