"""
10.	Дано ціле число N (> 0).  Знайти значення виразу 1.1 - 1.2 + 1.3 - ... (N доданків, знаки чергуються).  Умовний оператор не використовувати.
"""
userNumber = int(input('Введіть число: '))
resultSum = 0
numberStr = '1.'
multiplaer = 1
for i in range(1, userNumber):
    numberStr = '1.'
    tempNumStr = numberStr + str(i)
    resultSum += float(tempNumStr) * multiplaer
    multiplaer = multiplaer * -1

print('Значення виразу = ', resultSum)
input()