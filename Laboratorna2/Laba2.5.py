"""
5.	Дано ціле число. Вивести його рядок-опис виду «від'ємне парне число», «нульове число», «додатне непарне число» і т. д.
"""
userNumber = int(input('Введіть число :'))
resultAnsver = ''
if userNumber == 0:
    resultAnsver = 'Нульове'
elif userNumber > 0:
    resultAnsver = 'Додатне'
else:
    resultAnsver = 'Відємне'
print(userNumber % 2)
if userNumber != 0 and userNumber % 2:
    resultAnsver += " непарне"
elif userNumber != 0:
    resultAnsver += ' парне'

print('Число :', resultAnsver)
input()