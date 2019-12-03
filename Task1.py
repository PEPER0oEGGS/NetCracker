string = int(input())
k = string
lenOfK = 0  # длинна числа
while k > 0:
    k = int(k / 10)
    lenOfK += 1

LastRight = int(lenOfK / 2)  # Середина справа
FirsrtLeft = lenOfK - 1  # Последний элемент
allfine = True  # Маркер палиндром
k = 0  # первый элемент
while LastRight > k:
    a = int((string / (10 ** FirsrtLeft)) % 10)
    b = int(string / (10 ** k) % 10)
    if not a == b:
        allfine = False
        break
    k += 1
    FirsrtLeft -= 1

##if string == string[::-1]:
if allfine:
    print("YES")
else:
    print("NO")