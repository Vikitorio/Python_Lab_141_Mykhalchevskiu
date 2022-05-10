"""
5.	Описати функцію RectPS (x1, y1, x2, y2, P, S), яка обчислює периметр P і площу S прямокутника зі сторонами,
 паралельними осям координат, за координатами (x1, y1), (x2, y2) його протилежних вершин (x1, y1, x2, y2 - вхідні,
  P і S - вихідні параметри дійсного типу). За допомогою цієї функції знайти периметри і площі трьох
"""
def ReactPS(x1, y1, x2, y2):
    firstSide = abs(x1 - x2)
    secondSide = abs(y1 - y2)
    P = firstSide * 2 + secondSide*2
    S = firstSide * secondSide
    return 'P = ' + str(P) + '\nS = ' + str(S)

for i in range (3):
    x1 = int(input("Введіть X1: "))
    y1 = int(input("Введіть Y1: "))
    x2 = int(input("Введіть X2: "))
    y2 = int(input("Введіть Y1: "))
    print(ReactPS(x1, y1, x2, y2))
input()