"""
5.	Описати функцію Sin1 (x, ε) дійсного типу (параметри x, ε - дійсні, ε> 0),
 знаходить наближене значення функції sin (x):3 / (3!) + x5 / (5!) - ... + (-1) n · x2 · n +  1 / ((2 · n + 1)!) + ....
sin (x) = x - x
В сумі враховувати всі складові, модуль яких більше ε.
За допомогою Sin1 знайти наближене значення синуса для даного x при шести даних ε.

"""

def Sin1(x,eps):
    if eps <= 0:
        print("eps <= 0")
    curent = x
    result = x
    i = 3
    while abs(curent) > eps:
        curent *= (-1) * x * x / ((i-1)*i)
        i += 2
        result += curent
    return result

for i in range(3):
    userX = int(input('Введіть x: '))
    userEps = float(input('Введіть eps: '))
    print('sin(X) = ', Sin1(userX, userEps))

input()