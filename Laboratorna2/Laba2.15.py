"""15.	Дано координати (x; y) точки і радіус кола (r).  Визначити чи належить дана точка колі, якщо його центр знаходиться на початку координат. """
import math

print("Введите координаты точки и радиус круга")
xOfPoint = float(input("Введіть координату Х: "))
yOfPoint = float(input("Введіть координату Y: "))
RofCircle= float(input("Введіть R: "))

Hipotenusa = math.sqrt(xOfPoint ** 2 + yOfPoint ** 2)

if Hipotenusa <= RofCircle:
    print("Точка належить до кола")
else:
    print("Точка не належить до кола")

input()