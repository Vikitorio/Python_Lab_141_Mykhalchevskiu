"""
10.	Дано рядки S, S1 і S2.  Замінити в рядку S останнє входження рядка S1 на рядок S2.
"""
def replaceLastOccurrence(userStr, remove, add):
    return add.join(userStr.rsplit(remove, 1))


userStrMain = input('Введіть рядок: ')
userStrRemove = input('Введіть рядок який потрібно замінити: ')
userStrAdd = input('Введіть рядок яким замінити: ')

print(replaceLastOccurrence(userStrMain, userStrRemove, userStrAdd))

input()