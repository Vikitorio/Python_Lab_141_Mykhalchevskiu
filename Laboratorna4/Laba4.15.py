"""
15.	У списку чисел перевірити, чи всі елементи є унікальними, тобто кожне число зустрічається тільки один раз.
"""

def isContainDubles(str):
    for i in range(len(str)):
        if str[i].isdigit() and str.count(str[i]) > 1:
            return "Містить дублікати"
    return "Без дублікатів"


userStr = input("Введіть список чисел: ")
print(isContainDubles(userStr))
input()

