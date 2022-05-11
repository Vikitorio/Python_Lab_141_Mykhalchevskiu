"""
20. Присвоїти цілій змінній d першу цифру з дробової частини позитивного дійсного числа x.
"""
userNum = input('Введіть дробове число: ')

if userNum.count(','):
    userNum = userNum.split(',')
    resultB = userNum[1][0]
    print("Перша дробова цифра числа : ", resultB)
elif userNum.count('.'):
    userNum = userNum.split('.')
    resultB = userNum[1][0]
    print("Перша дробова цифра числа : ", resultB)
else:
    print("Число не дробове!!!!")

input()