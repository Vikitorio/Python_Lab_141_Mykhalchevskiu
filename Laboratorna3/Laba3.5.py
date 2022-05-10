"""
5.	Підрахувати k - кількість тризначних натуральних чисел, сума цифр яких дорівнює n (1≤n≤27).  Операції ділення не використовувати.
"""
userNum = int(input('Введіть n: '))
resultNum = 0
for i in range(100, 999):
    strI = str(i)
    compare = int(strI[0]) + int(strI[1]) + int(strI[2])
    if compare == userNum:
        resultNum += 1
print(resultNum, 'чисел')
input()