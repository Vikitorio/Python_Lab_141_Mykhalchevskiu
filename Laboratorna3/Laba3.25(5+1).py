"""
6.	Логічній змінній t присвоїти значення true або false залежно від того, є натуральне число k ступенем 3 чи ні.
"""

userNum = int(input())
def isSqrtOfK(Num):
    value = 1
    while (value < Num):
        value *= 3
    return value == Num
t = isSqrtOfK(userNum)
print('Т -', t)
input()