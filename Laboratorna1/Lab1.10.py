"""
10.	Даний розмір файла в байтах. Використовуючи операцію ділення без залишку,
 знайти кількість повних кілобайтів, які займає даний файл (1 кілобайт = 1024 байта).
"""

def byteToKilobyte(programWeight):
    return programWeight//1024


programWeightByte = int(input("Введіть розмір фалу : "))
print("Программа важить : ", byteToKilobyte(programWeightByte), " Кілобайт")
input()