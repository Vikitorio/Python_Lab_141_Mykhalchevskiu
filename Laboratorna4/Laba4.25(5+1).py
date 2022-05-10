"""
6.	Дано рядок.  Якщо в цьому рядку буква f зустрічається тільки один раз, виведіть її індекс.
  Якщо вона зустрічається два і більше разів, виведіть індекси її першої і останньої появи.
  Якщо буква f в цьому рядку не зустрічається, нічого не виводьте.
"""
userStr = input('Введіть строку: ')

def indexOfF(userstr):
    countF = userstr.count('f')
    if countF == 0:
        return ''
    elif countF > 1:
        return 'Перший індекс f :' + str(userstr.index('f')) + ', Останній індекс :' + str(userstr.rindex('f'))
    else:
        return 'Индекс f: ' + str(userstr.index('f'))

print(indexOfF(userStr))
input()
