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
Check_Number = int(input())
Buffer = Check_Number
Reverse_Number = 0

while Buffer > 0:
    Reverse_Number = Reverse_Number * 10
    Reverse_Number += Buffer % 10
    Buffer = int(Buffer / 10)

if (Reverse_Number - Check_Number) == 0:
    print("YES")
else:
    print("NO")
