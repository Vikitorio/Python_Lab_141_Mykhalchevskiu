"""
20.	Дано список чисел.  Порахуйте, скільки в ньому пар елементів, рівних один одному.
 Вважається, що будь-які два елементи, рівні один одному, утворюють одну пару, яку необхідно порахувати.
"""

def countPairs(usstr):
    sum = 0
    usstr = list(usstr)
    usstr.sort()
    for i in usstr:
        sum += usstr.count(i) // 2
        usstr = usstr[usstr.count(i):]
    return sum


userStr = input('Введіть строку чисел: ')

print(countPairs(userStr), '- пари')
input()