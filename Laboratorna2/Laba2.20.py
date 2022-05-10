"""
20.	Дано ціле число, яке лежить в діапазоні 1-999.  Вивести його рядок-опис виду «парне двозначне число», «непарне тризначне число» і т. Д.
"""

numberCount = {'1': 'однозначне', '2': 'двозначне', '3': 'тризначне'}

userNumber = input('Введіть число ')
resultAnswer = ''
if int(userNumber) % 2:
    resultAnswer += 'Непарне '
elif int(userNumber) != 0:
    resultAnswer += 'Парне '
resultAnswer += numberCount[str(len(userNumber))]
print(resultAnswer)
input()