"""
20.	Дано дійсне число ε (> 0). Послідовність дійсних чисел AK визначається наступним чином:
A1 = 1, A2 = 2, AK = (AK-2 + 2 • AK-1) / 3, K = 3, 4, ....
Знайти перший з номерів K, для яких виконується умова | AK - AK-1 | <Ε, і вивести цей номер,
 а також числа AK-1 і AK.
"""
userNum = float(input('Введіть число ε: '))
resultStr = ''
def FindNumToEps(n):
    if n == 1 :
        return 1
    elif n == 2:
        return 2
    return (FindNumToEps(n-2) + 2 * FindNumToEps(n-1)) / 3


i = 3
while i:

    tempNum = FindNumToEps(i)
    tempNumPust = FindNumToEps(i-1)
    if (abs(tempNum - tempNumPust) < userNum):
        resultStr = 'K = ' + str(i) + '\n' + 'AK-1 = ' + str(tempNumPust) + '\n' + 'AK = ' + str(tempNum)
        break
    i += 1
print(resultStr)
input()