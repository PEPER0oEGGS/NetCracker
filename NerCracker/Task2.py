Alfa = int(input())
Onser = Alfa
Dec = 10
F = 0
Y = 0
mem = Alfa
if Alfa == 1:
   print(1)
elif Alfa == 0:
    print(1)
else:
    while True:
        mem = mem * Alfa
        F = mem % 10 + Y
        Onser = Onser + Dec * (F % 10)
        Dec = Dec*10
        Y = int((mem / 10) % 10)+int((F/10))
        mem = int(F % 10)
        if Y+(F*Alfa) == Alfa:
            print(Onser)
            print("*"+ str(Alfa) + "=")
            print(Onser*Alfa)
            break