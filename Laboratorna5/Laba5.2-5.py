"""
5.	Описати функцію TriangleP (a, h), що знаходить периметр рівнобедреного трикутника за його основою a і висотою h,
 проведеною до основи (a і h - дійсні). За допомогою цієї функції знайти периметри трьох трикутників,
  для яких дані основи і висоти. Для знаходження сторони b трикутника використовувати теорему
  Піфагора: b2 = (a / 2) 2 + h2.
"""

def TriangleP(a ,h):
    tripletSide = ((a/2) ** 2 + h ** 2) ** 0.5
    print(tripletSide)
    return tripletSide * 2 + a

for i in range(3):
   a = int(input("Введіть довжину основи a: "))
   h = int(input("Введіть довжину висоти h: "))
   print('P = ', TriangleP(a, h))
input()