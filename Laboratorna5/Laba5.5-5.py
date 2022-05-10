"""
5.	Описати функцію RearRange(x, y), яка перевіряє, чи можливо переставивши букви в слові х отримати слово y.
"""
def RearRange(word1, word2):
    word1.sort()
    word2.sort()
    if len(word1) != len(word2):
        return 'Неможливо'
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            return 'Неможливо'
    return 'Можливо'

userWord = list(input("Введіть перше слово: "))
checkWord = list(input('Введіть друге слово: '))
print(RearRange(userWord, checkWord))
input()