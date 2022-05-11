import math
"""
5.	Обчислити дробову частину середнього геометричного трьох заданих позитивних чисел.
"""
suma = 0
count = 3
for i in range(count):
    a = int(input("enter the number : "))
    suma += a
suma = suma**(1/3)
print("дробова частина = ", suma-int(suma))
input()


