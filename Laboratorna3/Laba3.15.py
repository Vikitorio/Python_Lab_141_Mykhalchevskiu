"""
15.	Дано ціле число N (> 0). Послідовність дійсних чисел AK визначається наступним чином: A0 = 1, AK = (AK-1 + 1) / K, K = 1, 2, ....Вивести елементи A1, A2, ..., AN.
"""

userNum = int(input('Введіть N: '))
resultStr = ''
AKpast = 1
for i in range(1, userNum+1):
    AKpast = (AKpast + 1) / i
    if i == userNum:
        resultStr += 'A' + str(i) + ' = ' + str(AKpast) + '.'
        break
    resultStr += 'A' + str(i) + ' = ' + str(AKpast) + ', '
print(resultStr)
input()